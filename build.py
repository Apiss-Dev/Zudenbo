#!/usr/bin/env python3
"""
build.py — Static site generator for the Zudenbo Cakra Utama website.

WHY THIS EXISTS
----------------
Previously the site loaded header/nav/footer at RUNTIME in the browser
(via fetch()). That caused a visible "flash/glitch" every time you moved
between pages, because the browser had to draw the page first, then wait
for a network request, then pop the header/nav/footer in afterwards.

This script solves that by doing the assembly ONCE, on your computer,
BEFORE you upload anything. It reads:
  - partials/header.html   (shared header)
  - partials/nav.html      (shared sidebar menu)
  - partials/footer.html   (shared footer)
  - content/<page>.html    (the unique content of each page)
  - build_manifest.json    (title + meta description per page)
and combines them into complete, final .html files sitting at the
project root — exactly like the original hand-written files, except now
you only maintain ONE copy of the header/nav/footer.

HOW TO USE
----------
Whenever you edit anything in partials/ or content/, just run:

    python3 build.py

...and all pages at the root will be regenerated. Then upload the
project root to your hosting as usual. No Python is needed on the
server — the output is 100% plain HTML/CSS/JS.
"""

import json
import re
from pathlib import Path
from datetime import date
from bs4 import BeautifulSoup

ROOT = Path(__file__).parent
DOMAIN = "https://www.zudenbocakrautama.com"  # TODO: replace with your real .com domain

HEAD_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title_full}</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="{domain}/{canonical_path}" />

  <!-- Favicon -->
  <link rel="icon" type="image/x-icon" href="assets/images/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/images/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="assets/images/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="assets/images/apple-touch-icon.png">

  <link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Source+Sans+3:wght@300;400;600;700&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="assets/css/style.css"/>
</head>
<body>

{header}

  <!-- LAYOUT -->
  <div id="layout">

{nav}

    <!-- CONTENT -->
    <main id="main-content">
      <div class="page-content">
{content}
      </div>
    </main>

  </div>

{footer}

  <script src="assets/js/main.js"></script>
</body>
</html>
"""


def indent(html, spaces):
    pad = " " * spaces
    return "\n".join(pad + line if line.strip() else line for line in html.splitlines())


def build_nav_for_page(nav_html, current_page):
    """Return a copy of nav.html with the correct 'active' (and dropdown
    'open') classes applied for the given current page filename."""
    soup = BeautifulSoup(nav_html, "html.parser")

    for link in soup.select("#sidebar nav a"):
        href = link.get("href")
        if href == current_page:
            classes = link.get("class", [])
            if "active" not in classes:
                classes.append("active")
            link["class"] = classes

            # If this is a submenu link, also mark the parent "Technical"
            # link active and open its dropdown.
            parent_li = link.find_parent("li", class_="has-dropdown")
            if parent_li and "nav-parent" not in link.get("class", []):
                li_classes = parent_li.get("class", [])
                if "open" not in li_classes:
                    li_classes.append("open")
                parent_li["class"] = li_classes

                parent_link = parent_li.find("a", class_="nav-parent")
                if parent_link:
                    pl_classes = parent_link.get("class", [])
                    if "active" not in pl_classes:
                        pl_classes.append("active")
                    parent_link["class"] = pl_classes

    return str(soup)


def main():
    manifest = json.loads((ROOT / "build_manifest.json").read_text(encoding="utf-8"))
    header_html = (ROOT / "partials" / "header.html").read_text(encoding="utf-8")
    nav_html_raw = (ROOT / "partials" / "nav.html").read_text(encoding="utf-8")
    footer_html = (ROOT / "partials" / "footer.html").read_text(encoding="utf-8")

    # Keep the footer year current at build time too.
    current_year = str(date.today().year)
    footer_html = re.sub(
        r'(<span id="copyright-year">)\d{4}(</span>)',
        rf"\g<1>{current_year}\g<2>",
        footer_html,
    )

    built = []
    for page, meta in manifest.items():
        content_path = ROOT / "content" / page
        if not content_path.exists():
            print(f"  ! Skipping {page}: no content/{page} file found")
            continue

        content_html = content_path.read_text(encoding="utf-8")
        nav_html = build_nav_for_page(nav_html_raw, page)
        canonical_path = "" if page == "index.html" else page

        final_html = HEAD_TEMPLATE.format(
            title_full=meta["title_full"],
            description=meta["description"],
            domain=DOMAIN,
            canonical_path=canonical_path,
            header=indent(header_html.strip(), 2),
            nav=indent(nav_html.strip(), 4),
            content=content_html,
            footer=indent(footer_html.strip(), 2),
        )

        (ROOT / page).write_text(final_html, encoding="utf-8")
        built.append(page)

    print(f"Built {len(built)} pages:")
    for p in built:
        print(f"  - {p}")


if __name__ == "__main__":
    main()

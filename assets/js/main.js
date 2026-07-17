/* ============================================================
   MAIN.JS
   Header/nav/footer are now baked directly into every HTML file
   by build.py (no runtime fetch = no flash/glitch when navigating).
   This file only handles page INTERACTIVITY:
   - Mobile/tablet hamburger menu (open/close the sidebar)
   - Sidebar dropdown ("Technical" submenu)
   - Contact form submission
   ============================================================ */

(function () {

  /* ---------------------------------------------------------
     1. Hamburger menu (tablet & mobile off-canvas sidebar)
     --------------------------------------------------------- */
  function initMobileNav() {
    var toggleBtn = document.getElementById('nav-toggle');
    var sidebar = document.getElementById('sidebar');
    var backdrop = document.getElementById('nav-backdrop');
    if (!toggleBtn || !sidebar || !backdrop) return;

    function openNav() {
      sidebar.classList.add('open');
      backdrop.classList.add('visible');
      toggleBtn.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden'; // prevent background scroll
    }
    function closeNav() {
      sidebar.classList.remove('open');
      backdrop.classList.remove('visible');
      toggleBtn.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }

    toggleBtn.addEventListener('click', function () {
      var isOpen = sidebar.classList.contains('open');
      isOpen ? closeNav() : openNav();
    });

    backdrop.addEventListener('click', closeNav);

    // Close the drawer automatically when a nav link is tapped (mobile UX)
    sidebar.querySelectorAll('nav a').forEach(function (link) {
      link.addEventListener('click', function () {
        if (window.innerWidth <= 1024) closeNav();
      });
    });

    // If the window is resized back up to desktop width, make sure
    // the drawer state/backdrop/scroll-lock are reset.
    window.addEventListener('resize', function () {
      if (window.innerWidth > 1024) closeNav();
    });
  }

  /* ---------------------------------------------------------
     2. Dropdown open/close (arrow button only — link still
        navigates normally when clicked)
     --------------------------------------------------------- */
  function initDropdown() {
    var dropdownItems = document.querySelectorAll('#sidebar .has-dropdown');

    dropdownItems.forEach(function (item) {
      var toggleBtn = item.querySelector('.dropdown-toggle');
      if (!toggleBtn) return;

      toggleBtn.addEventListener('click', function (e) {
        e.preventDefault();
        var isOpen = item.classList.contains('open');
        dropdownItems.forEach(function (d) { d.classList.remove('open'); });
        if (!isOpen) item.classList.add('open');
      });
    });
  }

  /* ---------------------------------------------------------
     3. Footer year — keeps it current even if a tab stays open
        across a New Year (build.py already bakes in the correct
        year at build time, this is just a safety net)
     --------------------------------------------------------- */
  function setCopyrightYear() {
    var yearEl = document.getElementById('copyright-year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();
  }

  /* ---------------------------------------------------------
     4. Contact form — submits to Formspree so it works from
        any device, even without an email app installed.

        SETUP REQUIRED: create a free form at https://formspree.io
        and replace YOUR_FORM_ID below AND in contact.html's
        <form action="..."> attribute.
     --------------------------------------------------------- */
  var FORMSPREE_ENDPOINT = 'https://formspree.io/f/YOUR_FORM_ID';

  function initContactForm() {
    var form = document.getElementById('contact-form');
    if (!form) return;

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var submitBtn = form.querySelector('.btn-submit');
      var successBox = document.getElementById('form-success');
      var errorBox = document.getElementById('form-error');

      submitBtn.disabled = true;
      submitBtn.textContent = 'Sending...';

      fetch(FORMSPREE_ENDPOINT, {
        method: 'POST',
        headers: { 'Accept': 'application/json' },
        body: new FormData(form)
      })
        .then(function (response) {
          if (response.ok) {
            if (successBox) successBox.style.display = 'block';
            if (errorBox) errorBox.style.display = 'none';
            form.reset();
          } else {
            throw new Error('Submission failed');
          }
        })
        .catch(function () {
          if (errorBox) errorBox.style.display = 'block';
          if (successBox) successBox.style.display = 'none';
        })
        .finally(function () {
          submitBtn.disabled = false;
          submitBtn.textContent = 'Send Message';
        });
    });
  }

  /* ---------------------------------------------------------
     BOOT
     --------------------------------------------------------- */
  document.addEventListener('DOMContentLoaded', function () {
    initMobileNav();
    initDropdown();
    setCopyrightYear();
    initContactForm();
  });

})();

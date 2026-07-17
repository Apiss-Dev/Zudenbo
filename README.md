# Website PT Zudenbo Cakra Utama

## Struktur Folder

```
zudenbo-website/
├── index.html, about.html, dst.  ← FILE FINAL hasil build (jangan diedit langsung di sini!)
├── build.py                    ← jalankan ini setelah edit partials/ atau content/
├── build_manifest.json         ← judul & meta description tiap halaman
├── robots.txt                  ← petunjuk untuk Google/search engine
├── sitemap.xml                 ← daftar semua halaman untuk Google
├── partials/                   ← EDIT DI SINI untuk ubah semua halaman sekaligus
│   ├── header.html             ← logo + nama perusahaan + tombol hamburger
│   ├── nav.html                 ← menu sidebar kiri
│   └── footer.html             ← footer bawah
├── content/                    ← isi unik tiap halaman (paragraf, judul, dst.)
│   ├── index.html, about.html, dst.
└── assets/
    ├── css/style.css           ← semua warna & jarak asli + tambahan responsive
    ├── js/main.js              ← hamburger menu, dropdown, form kontak
    └── images/
        ├── logo.jpeg
        ├── favicon.ico
        ├── favicon-16x16.png
        ├── favicon-32x32.png
        └── apple-touch-icon.png
```

## Cara Maintenance (Sekali Edit, Semua Halaman Ikut Berubah)

1. Edit file di `partials/` (header/nav/footer) atau `content/` (isi halaman).
2. Jalankan di terminal:
   ```bash
   cd zudenbo-website
   python3 build.py
   ```
3. Selesai — semua 11 file `.html` di root otomatis di-generate ulang dengan
   perubahan tadi. Upload ulang ke hosting.

Contoh:
- Mau ganti alamat/kontak di **footer**? → edit `partials/footer.html` → `python3 build.py`
- Mau tambah/hapus/ubah urutan **menu**? → edit `partials/nav.html` → `python3 build.py`
- Mau ganti **logo atau nama perusahaan**? → edit `partials/header.html` → `python3 build.py`
- Mau ubah isi paragraf halaman About? → edit `content/about.html` → `python3 build.py`

Menu yang aktif (hijau ter-highlight) dan submenu "Technical" yang terbuka
otomatis dihitung oleh `build.py` sesuai halaman — Anda tidak perlu
menandai class `active` manual lagi.

**Catatan:** `python3` hanya dibutuhkan di komputer Anda untuk proses build.
Hasil akhirnya adalah file HTML/CSS/JS biasa — hosting Anda tidak perlu
Python sama sekali.

## 🔒 Keamanan Hosting

| File | Dipakai jika hosting Anda... |
|------|------------------------------|
| `.htaccess` | cPanel / shared hosting Apache|
| `_headers` | Netlify atau Cloudflare Pages |
| `vercel.json` | Vercel |

## Reponsive
Website sekarang menyesuaikan otomatis di semua ukuran layar:

- **Desktop (>1024px):** tampilan seperti desain asli — sidebar menu selalu
  terlihat di kiri.
- **Tablet & Mobile (≤1024px):** sidebar menu disembunyikan jadi menu
  "hamburger" (☰) di header. Tap ikon hamburger untuk membuka menu dari
  sisi kiri (muncul dengan animasi slide + overlay gelap di belakangnya),
  tap di luar menu atau pilih salah satu link untuk menutupnya lagi.
- **Mobile kecil (≤640px):** ukuran font, padding, dan grid kartu (card-grid)
  otomatis menyesuaikan supaya tetap nyaman dibaca di layar sempit.
- **Mobile sangat kecil (≤380px):** tagline "Engineering & MEP Services" di
  header disembunyikan supaya tidak sesak, logo sedikit diperkecil.

## Cara Testing di Komputer Sendiri

Karena `main.js` memuat partial dengan `fetch()`, file **tidak bisa dibuka
langsung** dengan cara double-click (`file://`) — browser akan blokir karena
alasan keamanan (CORS). Anda perlu menjalankan local server sederhana:

```bash
cd zudenbo-website
python3 -m http.server 8000
```

Lalu buka `http://localhost:8000` di browser. Ini hanya untuk testing lokal
— begitu di-upload ke hosting sungguhan (domain .com Anda), semuanya akan
berjalan normal tanpa perlu server khusus, karena semua hosting web otomatis
menjalankan protokol `http(s)://`.



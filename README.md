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

## ⚡ PENTING: Kenapa Sekarang Ada `build.py`?

Versi sebelumnya memuat header/nav/footer saat halaman dibuka di browser
(pakai JavaScript `fetch()`). Ini menyebabkan **efek "glitch"/flash** setiap
pindah halaman — halaman sempat kelihatan kosong sepersekian detik sebelum
header/menu "muncul".

Sekarang sudah diperbaiki dengan cara yang benar: **build.py menggabungkan
semuanya SEBELUM upload**, jadi setiap file HTML final sudah lengkap dari
awal — tidak ada jeda, tidak ada flash, perpindahan halaman langsung mulus
seperti website pada umumnya.

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

Tiga file konfigurasi keamanan sudah disediakan — **pakai HANYA SATU** sesuai
jenis hosting Anda, sisanya tidak akan berpengaruh (aman dibiarkan saja):

| File | Dipakai jika hosting Anda... |
|------|------------------------------|
| `.htaccess` | cPanel / shared hosting Apache (paling umum di Indonesia) |
| `_headers` | Netlify atau Cloudflare Pages |
| `vercel.json` | Vercel |

Isinya menambahkan security header standar: paksa HTTPS, `HSTS`,
`X-Content-Type-Options`, `X-Frame-Options`, `Content-Security-Policy` (sudah
di-scope supaya cuma izinkan Google Fonts + Formspree, sesuai yang dipakai
situs ini), dan `Permissions-Policy`.

**Checklist keamanan lain yang perlu Anda terapkan sendiri di sisi hosting:**

1. **Aktifkan SSL/HTTPS** (Let's Encrypt gratis) — biasanya tinggal 1 klik di
   cPanel/hosting panel Anda.
2. **Aktifkan 2FA** di akun registrar domain DAN akun hosting/cPanel — ini
   titik yang paling sering jadi sasaran (domain/hosting hijacking).
3. **Aktifkan domain lock** di registrar supaya domain tidak bisa
   dipindahtangankan tanpa izin.
4. Pertimbangkan pasang **Cloudflare** (gratis) di depan hosting Anda untuk
   proteksi DDoS + firewall tambahan.
5. **Jangan upload** `build.py`, `partials/`, `content/`, `build_manifest.json`
   ke server produksi — file-file itu hanya alat kerja lokal Anda, tidak
   perlu ikut di-hosting publik (mengurangi apa yang bisa dilihat orang lain
   soal struktur internal situs Anda).
6. Gunakan **SFTP**, bukan FTP biasa, saat upload file ke hosting (FTP
   biasa mengirim password tanpa enkripsi).
7. Aktifkan **backup otomatis** mingguan dari panel hosting Anda.



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

Semua breakpoint ini ada di `assets/css/style.css` bagian `/* RESPONSIVE */`
di baris paling bawah — bisa disesuaikan lagi kalau perlu.

## ⚠️ Yang WAJIB Anda Lakukan Sebelum Go-Live

1. **Ganti domain placeholder.**
   Saya menggunakan `https://www.zudenbocakrautama.com` sebagai domain
   sementara di `sitemap.xml`, `robots.txt`, dan tag `<link rel="canonical">`
   di setiap halaman. Cari-ganti (find & replace) semua kemunculan
   `zudenbocakrautama.com` dengan domain .com asli yang Anda beli.

2. **Aktifkan form kontak (Formspree).**
   Form di `contact.html` sebelumnya memakai `mailto:` yang tidak selalu
   berhasil (butuh aplikasi email ter-install di HP/laptop user). Sekarang
   sudah diganti supaya submit langsung terkirim dari server, tapi Anda
   perlu:
   - Daftar gratis di [formspree.io](https://formspree.io)
   - Buat form baru, salin Form ID yang diberikan
   - Ganti `YOUR_FORM_ID` di 2 tempat:
     - `assets/js/main.js` (variabel `FORMSPREE_ENDPOINT`)
     - `contact.html` (atribut `action` pada tag `<form>`)
   - Formspree tier gratis cukup untuk volume kontak website perusahaan kecil–menengah.

3. **Isi data placeholder.**
   Nomor telepon `+62 21 xxxx xxxx` dan WhatsApp `+62 8xx xxxx xxxx` di
   `partials/footer.html`... (nomor ini masih ada di `contact.html`, cari
   dan ganti dengan nomor asli perusahaan).

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

## Deploy ke Hosting

Upload seluruh isi folder `zudenbo-website/` (bukan folder itu sendiri,
tapi isinya) ke **document root** hosting Anda:
- cPanel: folder `public_html/`
- Netlify/Vercel: drag & drop seluruh folder
- Pastikan `index.html` berada tepat di root, bukan di dalam sub-folder,
  supaya `www.domainanda.com` langsung membuka halaman Home.

## Ringkasan Perbaikan yang Dilakukan

| # | Masalah | Perbaikan |
|---|---------|-----------|
| 1 | Tidak ada favicon | Ditambahkan (favicon.ico, PNG 16/32px, apple-touch-icon) dari logo asli |
| 2 | Tidak ada meta description | Ditambahkan di 11 halaman untuk SEO |
| 3 | Tidak ada robots.txt / sitemap.xml | Ditambahkan |
| 4 | Klik "Technical" tidak pernah membuka halamannya (selalu ke-preventDefault) | Tombol panah dipisah dari link teks — klik teks = navigasi normal, klik panah = buka/tutup submenu |
| 5 | Form kontak hanya `mailto:` (gagal jika tak ada app email) | Diganti ke submission via Formspree (perlu setup, lihat di atas) |
| 6 | Header/nav/footer di-copy 11×, sulit maintenance | Dipusatkan jadi 3 file di `partials/`, di-load otomatis oleh `main.js` |
| 7 | Tahun copyright hardcode manual | Otomatis mengikuti tahun berjalan (di-set ulang tiap kali `build.py` dijalankan) |
| 8 | Nav "active" state harus ditandai manual per halaman | Otomatis dihitung oleh `build.py` |
| 9 | Pindah halaman terasa "glitch"/flash | Header/nav/footer dibakukan (baked) ke setiap file HTML saat build — tidak ada lagi fetch runtime |
| 10 | Sidebar hilang total di HP (tidak ada cara buka menu) | Ditambahkan hamburger menu (☰) dengan slide-in drawer untuk tablet & mobile |
| 11 | Belum ada penyesuaian ukuran font/layout untuk berbagai ukuran layar | Ditambahkan breakpoint responsive lengkap: desktop, tablet, mobile, mobile kecil |

**Desain (warna, posisi, tata letak, tipografi) tidak ada yang diubah** —
semua nilai di `style.css` persis sama seperti file asli Anda.

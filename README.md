# 🕵️‍♂️ WXD Proxy Hunter (Residential & Elite Proxy Finder)

**WXD Proxy Hunter** adalah bot pencari proxy otomatis berkecepatan tinggi yang dirancang khusus untuk memisahkan proxy kualitas premium (**Residential ISP**) dari proxy server biasa (**Datacenter**).
Bot ini dibangun dengan arsitektur **Asynchronous (AsyncIO)** dan **Docker**, berjalan sangat ringan, dan memiliki fitur **Hybrid Mode** (bisa berjalan dengan atau tanpa Telegram).

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)
![SQLite](https://img.shields.io/badge/SQLite-WAL%20Mode-green.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)

---

## 🔥 Fitur Unggulan

* ✅ **Smart Residential Filter:** Memisahkan proxy ISP Rumahan (Indihome, Verizon, Comcast) yang tahan blokir dari proxy VPS/Datacenter.
* ✅ **Hybrid / Headless Mode:** Bot otomatis berjalan di terminal (CLI) jika Token Telegram kosong atau API down. Anti-Crash!
* ✅ **Resource Limiting:** Aman dijalankan dengan spesifikasi rendah karena bisa di setel manual sesuai keinginan (default: Max 1 CPU 50%, RAM 512MB).
* ✅ **Auto-Deduplication:** Proxy yang sudah ada di database tidak akan dicek ulang ke API ISP (Hemat Kuota).
* ✅ **SQLite WAL Mode:** Database super cepat, anti-lock saat ribuan data masuk bersamaan.

---

## 🛠️ Instalasi & Setup

Ikuti langkah-langkah ini satu per satu di terminal.

### 1. Download Repository
Ambil kode terbaru dari GitHub:

    git clone https://github.com/widodoxd/WXD-PROXY-HUNTER.git
    cd WXD-PROXY-HUNTER

### 2. Buat Konfigurasi
Copy file contoh konfigurasi menjadi file konfigurasi aktif:

    cp config.example.py config.py

Edit file tersebut menggunakan nano:

    nano config.py
    
    Panduan Edit:
    * BOT_TOKEN: Isi dengan token dari BotFather. (Kosongkan jika ingin mode tanpa Telegram).
    * ALLOWED_USER_ID: Isi dengan ID Telegram Anda (agar bot private).
    * Tekan Ctrl+O lalu Enter untuk Simpan, dan Ctrl+X untuk Keluar.

### 3. Jalankan Bot
Perintah ini akan membangun sistem (build) dan menjalankannya di background:

    docker compose up -d --build

### 4. Cek Status
Pastikan bot sudah berjalan normal dengan melihat log:

    docker compose logs -f

    (Tekan Ctrl + C pada keyboard untuk keluar dari tampilan log)

---

## 🎮 Cara Penggunaan

### A. Mode Telegram (GUI)
Jika Token Bot diisi, kirim perintah /start di Telegram. Panel berikut akan muncul:

| Tombol Menu         | Fungsi                                                        |
|---------------------|---------------------------------------------------------------|
| ▶️ START SCAN       | Memulai siklus pencarian proxy secara otomatis (Looping).     |
| 🛑 STOP             | Menghentikan proses pencarian.                                |
| 📄 LOG              | Cek status live bot dan statistik database terkini.           |
| 💾 DB Stats         | Melihat jumlah total proxy dan jumlah proxy Residential.      |
| 📥 RESIDENTIAL ONLY | 💎 Premium: Download file .txt khusus proxy ISP Rumahan.      |
| 📥 ALL (IP:PORT)    | Download semua proxy aktif format 1.1.1.1:8080.               |
| 🏳️ SET REGION       | Filter pencarian hanya negara tertentu (Contoh: ID, US, SG).  |

### B. Mode Server (CLI / Headless)
Jika Token Telegram kosong atau salah, bot akan otomatis masuk ke Mode Hantu:
1. Bot mendeteksi ketiadaan token.
2. Notifikasi Telegram dimatikan.
3. Proses mining tetap berjalan normal di background Terminal/CLI.
4. Hasil tetap disimpan ke Database dan File .txt.

---

## 📂 Lokasi File Output

Bot akan menyimpan hasil "buruan" secara otomatis di dalam folder project di VPS Anda:

* 📂 proxy_residential.txt  👉 List Premium (ISP Rumahan Only).
* 📂 proxy_active.txt       👉 Semua proxy aktif (Campur).
* 📂 type_proxy_active.txt  👉 Format URI (socks5://user:pass@ip:port).
* 📂 proxies.db             👉 Database utama SQLite.

---

## ⚙️ Perintah Admin VPS

Simpan perintah-perintah berguna ini:

**Mematikan Bot:**

    docker compose down

**Restart Bot (Refresh Cepat):**

    docker compose restart

**Update Bot (Jika ada fitur baru):**

    git pull
    docker compose up -d --build

---

## ⚠️ Disclaimer
Project ini dibuat untuk tujuan Edukasi, Riset Keamanan, dan Testing Jaringan.
Penggunaan proxy hasil scanning untuk aktivitas ilegal adalah tanggung jawab pengguna sepenuhnya. Gunakan dengan bijak.

---

**Dev:** widodoxd | **License:** MIT
EOF

cat << 'EOF' > README.md
# 🕵️‍♂️ WXD Proxy Hunter (Residential & Elite Proxy Finder)

**WXD Proxy Hunter** is a high-speed automatic proxy search bot designed specifically to find HIGH ANONYMITY (ELITE) proxies and separate premium quality proxies (**Residential ISP**) from standard server proxies (**Datacenter**).

Built with **Asynchronous (AsyncIO)** architecture and **Docker**, this bot runs very lightly and features a **Hybrid Mode** (operates with or without Telegram).

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)
![SQLite](https://img.shields.io/badge/SQLite-WAL%20Mode-green.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)

---

## 🔥 Key Features

* ✅ **Smart Residential Filter:** Separates block-resistant Home ISP proxies (Indihome, Verizon, Comcast) from VPS/Datacenter proxies.
* ✅ **Hybrid / Headless Mode:** The bot automatically runs in the terminal (CLI) if the Telegram Token is empty or the API is down. Anti-Crash!
* ✅ **Resource Limiting:** Safe to run on low-spec hardware as it can be manually tuned (Default: Max 1 CPU 50%, RAM 512MB).
* ✅ **Auto-Deduplication:** Proxies already in the database will not be re-checked against the ISP API (Saves Quota).
* ✅ **SQLite WAL Mode:** Super fast database, anti-lock when thousands of data entries arrive simultaneously.

---

## 🛠️ Installation & Setup

Follow these steps one by one in your terminal.

### 1. Download Repository
Get the latest code from GitHub:

    git clone https://github.com/widodoxd/WXD-PROXY-HUNTER.git
    cd WXD-PROXY-HUNTER

### 2. Create Configuration
Copy the example configuration file to the active configuration file:

    cp config.example.py config.py

Edit the file using nano:

    nano config.py

**Editing Guide:**
* `BOT_TOKEN`: Fill with the token from BotFather. (Leave empty if you want Telegram-less mode).
* `ALLOWED_USER_ID`: Fill with your Telegram ID (to keep the bot private).
* Press `Ctrl+O` then `Enter` to Save, and `Ctrl+X` to Exit.

### 3. Run the Bot
This command will build the system and run it in the background:

    docker compose up -d --build

### 4. Check Status
Ensure the bot is running normally by checking the logs:

    docker compose logs -f

    (Press Ctrl + C on your keyboard to exit the log view)

---

## 🎮 Usage

### A. Telegram Mode (GUI)
If the Bot Token is filled, send the `/start` command in Telegram. The following panel will appear:

| Menu Button         | Function                                                      |
|---------------------|---------------------------------------------------------------|
| ▶️ START SCAN       | Start automatic proxy search cycle (Looping).                 |
| 🛑 STOP             | Stop the search process.                                      |
| 📄 LOG              | Check live bot status and current database statistics.        |
| 💾 DB Stats         | View total proxy count and Residential proxy count.           |
| 📥 RESIDENTIAL ONLY | 💎 Premium: Download .txt file specifically for Home ISP.     |
| 📥 ALL (IP:PORT)    | Download all active proxies in 1.1.1.1:8080 format.           |
| 🏳️ SET REGION       | Filter search for specific countries only (e.g., ID, US, SG). |

### B. Server Mode (CLI / Headless)
If the Telegram Token is empty or invalid, the bot will automatically enter **Ghost Mode**:
1. Bot detects the absence of a token.
2. Telegram notifications are disabled.
3. The mining process continues normally in the background Terminal/CLI.
4. Results are still saved to the Database and .txt files.

---

## 📂 Output File Locations

The bot will automatically save the "hunt" results inside the project folder on your VPS:

* 📂 `proxy_residential.txt`  👉 Premium List (ISP/Home Only).
* 📂 `proxy_active.txt`       👉 All active proxies (Mixed).
* 📂 `type_proxy_active.txt`  👉 URI Format (socks5://user:pass@ip:port).
* 📂 `proxies.db`             👉 Main SQLite Database.

---

## ⚙️ VPS Admin Commands

Save these useful commands:

**Stop the Bot:**

    docker compose down

**Restart Bot (Fast Refresh):**

    docker compose restart

**Update Bot (If there are new features):**

    git pull
    docker compose up -d --build

---

## ⚠️ Disclaimer
This project is created for **Education, Security Research, and Network Testing** purposes.
Using scanned proxies for illegal activities is entirely the user's responsibility. Use wisely.

---

**Dev:** widodoxd | **License:** MIT
EOF

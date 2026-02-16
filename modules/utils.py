import logging
import time
import os

def setup_logging():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("telegram").setLevel(logging.WARNING)
    logging.getLogger("aiohttp").setLevel(logging.WARNING)
    logging.getLogger("asyncio").setLevel(logging.WARNING)

def save_formatted_proxies(proxy_list_dicts):
    try:
        timestamp = time.strftime('%Y-%m-%d %H:%M')
        
        # --- KELOMPOK 1: SEMUA PROXY (CAMPUR) ---
        
        # FILE 1: ALL IP:PORT
        with open("proxy_active.txt", "w") as f1:
            f1.write(f"=== ALL PROXY LIST ({timestamp}) ===\n")
            for p in proxy_list_dicts:
                f1.write(f"{p['ip']}\n")
        
        # FILE 2: ALL URI (protocol://ip:port)
        with open("type_proxy_active.txt", "w") as f2:
            f2.write(f"=== ALL PROXY URI ({timestamp}) ===\n")
            for p in proxy_list_dicts:
                proto = p['type'].lower()
                f2.write(f"{proto}://{p['ip']}\n")
        
        # --- KELOMPOK 2: RESIDENTIAL ONLY (PREMIUM) ---
        res_proxies = [p for p in proxy_list_dicts if p.get('category') == 'RESIDENTIAL']
        
        # FILE 3: RESIDENTIAL IP:PORT (Baru)
        with open("proxy_residential.txt", "w") as f3:
            # Kita buat polosan agar enak dicopy ke tools
            if res_proxies:
                for p in res_proxies:
                    f3.write(f"{p['ip']}\n")
            else:
                pass # Jangan tulis apa-apa jika kosong
        
        # FILE 4: RESIDENTIAL URI (Baru)
        with open("type_proxy_residential.txt", "w") as f4:
            if res_proxies:
                for p in res_proxies:
                    proto = p['type'].lower()
                    f4.write(f"{proto}://{p['ip']}\n")
            else:
                pass

        return True
    except Exception as e:
        print(f"[!] Gagal save file TXT: {e}")
        return False

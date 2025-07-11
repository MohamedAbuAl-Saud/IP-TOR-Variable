import os
import time
import random
import requests
import sys
import platform
from stem import Signal
from stem.control import Controller
import socket

TOR_PROXY = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def typing_effect(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def is_tor_running():
    try:
        with socket.create_connection(("127.0.0.1", 9050), timeout=3):
            with Controller.from_port(port=9051) as c:
                c.authenticate()
            return True
    except:
        return False

def get_ip():
    try:
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) Firefox/115.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4) AppleWebKit/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Edge/124.0.2478.80",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) Chrome/123.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 13; SM-G998B) Chrome/110.0.5481.65 Mobile",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/103.0.5060.134 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Firefox/97.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/537.36",
            "Mozilla/5.0 (Linux; Android 11; Pixel 5) Chrome/96.0.4664.45 Mobile",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/100.0.4896.75 Safari/537.36",
            "Mozilla/5.0 (iPad; CPU OS 15_3) Safari/604.1",
            "Mozilla/5.0 (X11; Linux x86_64) Chrome/90.0.4430.212 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64) Chrome/92.0.4515.107 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) Safari/605.1.15",
            "Mozilla/5.0 (Linux; Android 9; Redmi Note 8) Chrome/85.0.4183.127 Mobile",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Edge/90.0.818.56",
            "Mozilla/5.0 (X11; Fedora; Linux x86_64) Firefox/89.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4) Safari/604.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) Chrome/84.0.4147.89 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10; SM-A715F) Chrome/83.0.4103.106 Mobile",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/81.0.4044.129 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) Chrome/80.0.3987.149 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) Chrome/79.0.3945.130 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 8.1.0; Moto G5) Chrome/78.0.3904.108 Mobile",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/77.0.3865.90 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Firefox/76.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1) Safari/604.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) Safari/537.36",
            "Mozilla/5.0 (Linux; Android 7.0; LG-H930) Chrome/75.0.3770.101 Mobile",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) Chrome/74.0.3729.131 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) Chrome/73.0.3683.86 Safari/537.36",
            "Mozilla/5.0 (iPad; CPU OS 13_3_1) Safari/604.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) Safari/537.36",
            "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P) Chrome/70.0.3538.80 Mobile",
            "Mozilla/5.0 (Windows NT 6.1) Chrome/69.0.3497.100 Safari/537.36",
            "Mozilla/5.0 (X11; Fedora; Linux x86_64) Firefox/68.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) Safari/537.78.2",
            "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5) Chrome/67.0.3396.87 Mobile",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) Chrome/66.0.3359.181 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1) Safari/604.1",
            "Mozilla/5.0 (X11; Linux i686) Firefox/61.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8) Firefox/58.0",
            "Mozilla/5.0 (Linux; Android 4.4.2; SM-G900F) Chrome/55.0.2883.91 Mobile",
            "Mozilla/5.0 (Windows NT 6.1) Chrome/49.0.2623.112 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) Chrome/47.0.2526.111 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) Safari/534.57.2",
            "Mozilla/5.0 (Linux; Android 4.2.2; GT-I9505) Chrome/43.0.2357.93 Mobile",
            "Mozilla/5.0 (Windows NT 5.1) Chrome/40.0.2214.115 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Firefox/123.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) Safari/605.1.15 Version/17.0",
            "Mozilla/5.0 (X11; Linux x86_64) Chrome/122.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro) Chrome/121.0.0.0 Mobile",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0) Safari/604.1"
        ]
        ua = random.choice(user_agents)
        headers = {'User-Agent': ua}
        r = requests.get("https://api.ipify.org", proxies=TOR_PROXY, headers=headers, timeout=15)
        return f"{r.text.strip()} | UA: {ua}"
    except:
        return None

def banner(ip=None):
    clear_screen()
    typing_effect("\033[1;32m")
    print("┌" + "─" * 47 + "┐")
    print("│         Anonymity Over The Internet - DF Tool        │")
    print("├" + "─" * 47 + "┤")
    if ip:
        print(f"│  Current IP & UA:                                 │")
        print(f"│  {ip[:45]}{' ' * (45 - len(ip[:45]))}│")
    else:
        print("│  Current IP: Unknown                             │")
    print("└" + "─" * 47 + "┘")
    print("\033[0m")
    print("\033[1;34m┌────────────────────────────────────────────────────┐")
    print("│ Developer: @A_Y_TR                                │")
    print("│ Channel  : https://t.me/cybersecurityTemDF        │")
    print("└────────────────────────────────────────────────────┘\033[0m\n")
    print("\033[1;31m[!] Important Tip: Disable JavaScript & WebRTC manually in browser.\033[0m\n")

def reload_tor_ip():
    try:
        with Controller.from_port(port=9051) as c:
            c.authenticate()
            c.signal(Signal.NEWNYM)
            return True
    except:
        return False

def run_loop():
    try:
        interval = int(input("\n\033[1;36mTime between IP changes (seconds): \033[0m"))
        count = int(input("\033[1;36mHow many times? (0 = Infinite): \033[0m"))
    except:
        print("\033[1;31mInvalid input. Please enter numbers only.\033[0m")
        return

    print("\n\033[1;35m[•] Starting... Press Ctrl+C to stop.\033[0m\n")

    i = 0
    previous_ip = None

    while True:
        if count != 0 and i >= count:
            break

        success = reload_tor_ip()
        time.sleep(5)

        ip = get_ip()
        banner(ip)

        prefix = f"[{i+1}/{count}]" if count != 0 else "[∞]"

        if not success or ip is None:
            print(f"\033[1;31m{prefix} Failed to get new IP.\033[0m")
        elif ip == previous_ip:
            print(f"\033[1;33m{prefix} IP didn't change.\033[0m")
        else:
            print(f"\033[1;32m{prefix} New IP:\033[0m {ip}")
            previous_ip = ip
            i += 1 if count != 0 else 0

        time.sleep(random.randint(max(10, interval), interval + 3))

def main():
    typing_effect("\033[1;32m[•] Loading DF IP Masking Tool...\033[0m\n", 0.03)
    time.sleep(1)
    ip = get_ip()
    banner(ip)

    if not is_tor_running():
        print("\n\033[1;31m[✘] Tor is not running or control port is not accessible.\033[0m")
        print("\033[1;33m[!] Make sure Tor is started with 'tor' command and ControlPort is enabled.\033[0m")
        return

    run_loop()

if __name__ == "__main__":
    main()

# IP-TOR-Variable

---

🛡️ IPTOR - Full-System IP Masking over Tor

🔍 IPTOR is a tool designed to route your entire system traffic through the Tor network, especially for Kali Linux users. It provides high-level anonymity, with the ability to automatically change your IP at set intervals.


---

🚀 Project Contents

File	Description

IPTOR.py	Python script to automatically change IP using Tor and the stem library
Install-tor.sh	Shell script to fully configure your system to route all traffic through Tor
requirements.txt	Python dependencies (stem, requests)
	Step-by-step installation instructions



---

🧠 Tool Concept

Route all outgoing traffic through the Tor network

Automatically change the IP address every few minutes

Supports: Kali Linux / Debian-based systems

Handles errors and failures automatically

Beautiful, colored CLI interface



---

⚙️ How to Use

1️⃣ Install dependencies:


```
sudo apt update && sudo apt install -y tor proxychains python3 python3-pip iptables-persistent
pip3 install -r requirements.txt
```

2️⃣ Configure full-system Tor routing:

```
chmod +x Install-tor.sh
sudo ./Install-tor.sh
```

3️⃣ Launch the tool:

```
python3 IPTOR.py
```


---

🔄 Install.sh Does

This script automatically:

Installs Tor (if not already installed)

Edits torrc settings for transparent proxy

Configures iptables to route all traffic through Tor

Changes system DNS to route through Tor

Restarts the Tor service after applying changes

Shows a success message 🎯



---

🧱 Error Handling

The tool:

Verifies that Tor is running properly

Detects and reports control/authentication errors

Displays current IP address and success/failure of each change

Randomizes User-Agents to simulate real browser activity



---

🧪 Verify IP Anonymity

To check if your IP is hidden:

```
curl --socks5 127.0.0.1:9050 https://check.torproject.org
```

Or:
```
curl https://api.ipify.org
```

Compare the results and verify if your IP is masked 🔍

---
warning ⚠️

• Do not write in the request when running the tool to change the IP for less than 10 seconds, otherwise a problem will occur⚠️
----

---

🧠 Additional Tips

It is recommended to disable JavaScript and WebRTC in your browser

When using tools or browsers manually, run them with proxychains:

```
proxychains firefox
```


---

👨‍💻 Developer Info

Name: القيـــــــــــــــآدهہ‌‏ آلزعيـــم

Telegram: t.me/@A_Y_TR

Channel: https://t.me/cybersecurityTemDF



---

🧷 License

This project is open-source for personal and educational use only.
Illegal use is strictly prohibited. 👌


---




#!/bin/bash

clear
GREEN='\033[1;32m'
RED='\033[1;31m'
BLUE='\033[1;34m'
YELLOW='\033[1;33m'
RESET='\033[0m'

echo -e "${BLUE}╔═══════════════════════════════════════════════╗"
echo -e "${BLUE}║     ${YELLOW}DF - Full TOR Routing & Tool Launcher     ${BLUE}║"
echo -e "${BLUE}╚═══════════════════════════════════════════════╝${RESET}\n"

sleep 1

echo -e "${GREEN}[✓] Updating & installing dependencies...${RESET}"
sudo apt update && sudo apt install tor proxychains python3 python3-pip iptables-persistent netfilter-persistent -y || {
    echo -e "${RED}[✘] Failed to install packages.${RESET}"
    exit 1
}

echo -e "${GREEN}[✓] Installing Python libraries...${RESET}"
pip3 install stem requests || {
    echo -e "${RED}[✘] Failed to install Python modules.${RESET}"
    exit 1
}

echo -e "${GREEN}[✓] Enabling & starting TOR service...${RESET}"
sudo systemctl enable tor
sudo systemctl start tor

TORRC_PATH="/etc/tor/torrc"
if grep -q "TransPort 9040" "$TORRC_PATH"; then
    echo -e "${YELLOW}[!] Tor already configured for Transparent Proxy.${RESET}"
else
    echo -e "${GREEN}[✓] Updating torrc file...${RESET}"
    sudo bash -c "cat >> $TORRC_PATH" <<EOF

# Transparent Proxy Mode
VirtualAddrNetworkIPv4 10.192.0.0/10
AutomapHostsOnResolve 1
TransPort 9040
DNSPort 5353
ControlPort 9051
CookieAuthentication 0
EOF
fi

echo -e "${GREEN}[✓] Flushing old iptables rules...${RESET}"
sudo iptables -F
sudo iptables -t nat -F

echo -e "${GREEN}[✓] Applying iptables rules for TOR routing...${RESET}"
sudo iptables -t nat -A OUTPUT -m owner ! --uid-owner debian-tor -p tcp --syn -j REDIRECT --to-ports 9040
sudo iptables -t nat -A OUTPUT -m owner ! --uid-owner debian-tor -p udp --dport 53 -j REDIRECT --to-ports 5353
sudo iptables -A OUTPUT -o lo -j ACCEPT
sudo iptables -A OUTPUT -m owner --uid-owner debian-tor -j ACCEPT
sudo iptables -A OUTPUT -p tcp --syn -j REJECT

echo -e "${GREEN}[✓] Saving iptables rules...${RESET}"
sudo netfilter-persistent save

echo -e "${GREEN}[✓] Setting DNS to 127.0.0.1 ...${RESET}"
sudo bash -c "echo 'nameserver 127.0.0.1' > /etc/resolv.conf"

echo -e "${GREEN}[✓] Restarting TOR service...${RESET}"
sudo systemctl restart tor

echo -e "\n${YELLOW}[!] Verifying TOR Routing...${RESET}"
sleep 2
curl --socks5 127.0.0.1:9050 https://check.torproject.org || echo -e "${RED}[✘] Failed to check TOR connection.${RESET}"

# Check if IPTOR.py exists
if [ ! -f "IPTOR.py" ]; then
    echo -e "\n${RED}[✘] IPTOR.py not found in current directory!${RESET}"
    echo -e "${YELLOW}[!] Please place it in: $(pwd)${RESET}"
    exit 1
fi

echo -e "\n${GREEN}[✓] All setup done successfully!${RESET}"
echo -e "${BLUE}──────────────────────────────────────────────${RESET}"
echo -e "${YELLOW}[>] Launching IPTOR.py via python3...${RESET}\n"
sleep 2
python3 IPTOR.py || {
    echo -e "${RED}[✘] Failed to run IPTOR.py. Check for issues.${RESET}"
    exit 1
}

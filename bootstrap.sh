#!/bin/bash
echo "[+] Bootstrapping Personnel Management System"
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git

git clone https://github.com/paracryptid/personnel-management-system.git
cd personnel-management-system
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

echo "[+] Starting app..."
python app.py

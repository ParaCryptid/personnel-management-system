
#!/bin/bash

echo "[*] Creating secure AES key and IV..."
sudo mkdir -p /etc/personnel-system
sudo head -c 32 /dev/urandom > /etc/personnel-system/aes_key.bin
sudo head -c 16 /dev/urandom > /etc/personnel-system/aes_iv.bin
sudo chmod 600 /etc/personnel-system/aes_*.bin
echo "[+] AES keys created and secured at /etc/personnel-system"

echo "[*] Installing Python packages..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "[*] Setting up systemd service..."
sudo cp personnel-app.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable personnel-app.service
sudo systemctl start personnel-app.service
sudo systemctl status personnel-app.service --no-pager

echo "[*] Complete. The app is running on 127.0.0.1:5006"

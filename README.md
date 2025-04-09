
# Personnel Management System

A fully offline, self-hosted, and military-grade secure system for analyzing and encrypting personnel data. No third-party services used. Designed for hardened environments.

---

## 🔐 Features

- Encrypted personnel data processing (AES-256)
- AI-powered analytics (sentiment + data summaries)
- Real-time secure WebSocket communication
- Hardened Flask app with strict headers (via Talisman)
- Runs on `systemd`, reverse-proxied through Nginx
- No external cloud calls; completely local and auditable

---

## 📦 Installation

### Requirements
- Ubuntu 22.04+ or any Unix-like OS
- Python 3.9+
- Git, curl, sudo

### 1. Clone Repo & Run Setup
```bash
git clone git@github.com:paracryptid/personnel-management-system.git
cd personnel-management-system
chmod +x setup.sh
./setup.sh
```

### 2. Setup Nginx (Optional)
```bash
sudo cp nginx.conf /etc/nginx/sites-available/personnel
sudo ln -s /etc/nginx/sites-available/personnel /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

Nginx will reverse proxy to 127.0.0.1:5006 — perfect for a Cloudflare Tunnel setup.

---

## 🛡️ Security

- Only local interfaces exposed
- CSP, Strict-Transport headers enabled
- SocketIO CORS locked
- Randomized, secured AES key & IV in `/etc/personnel-system/`

---

## 🖥 Supported Platforms

- ✅ Ubuntu 22.04+ / Debian
- ✅ macOS (via Homebrew + Python3)
- ✅ Windows (via WSL2)

---

## 🔧 Development
To run manually:
```bash
source venv/bin/activate
python3 app.py
```

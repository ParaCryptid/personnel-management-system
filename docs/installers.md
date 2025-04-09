# Installation Guide

## 🐧 Linux
You can install using the `.deb` package:
```bash
sudo dpkg -i personnel-management-system-1.0.0.deb
```

Or run the portable `.AppImage`:
```bash
chmod +x personnel-management-system-1.0.0.AppImage
./personnel-management-system-1.0.0.AppImage
```

## 🪟 Windows
Use the standalone `.exe` installer:
- Double-click to launch
- No installation needed (portable)

## 🖥 macOS *(coming soon)*
Build manually using Python 3.11:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

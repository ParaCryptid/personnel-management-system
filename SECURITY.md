
# SECURITY OVERVIEW

This system is designed for high-risk, sensitive deployments in disconnected, offline, or hardened environments.

---

## 🔐 Core Security Measures

- AES-256-CFB encryption for stored data
- All encryption keys stored in /etc/personnel-system (permissions: 600)
- Role-based local authentication using bcrypt-hashed passwords
- Flask session tokens signed and validated
- WebSockets restricted (CORS off, no public access)
- Strict Content Security Policy (via Flask-Talisman)
- HTTPS headers enforced (when used behind Nginx)
- Cloudflare Tunnel-safe (runs only on localhost)
- Self-destruct mechanism possible via future systemd hook

---

## 🛡 Operational Security

- No external services or telemetry
- AI models load from local files only
- Local logs and encrypted audit records only
- CLI tool for airgapped data access and ops

---

## 🔒 Permissions & Access

- App runs under www-data or restricted service user
- Systemd used for isolated process control
- AppArmor profile can be added for advanced isolation

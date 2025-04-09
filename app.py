
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from transformers import pipeline
import pandas as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from flask_talisman import Talisman
import os
import json

app = Flask(__name__)
Talisman(app, content_security_policy={
    'default-src': ''self'',
    'script-src': ''self'',
    'style-src': ''self'',
    'img-src': ''self'',
    'connect-src': ''self'',
})

# Restrict CORS and large payloads
socketio = SocketIO(app, cors_allowed_origins=[], max_http_buffer_size=4096)

# Load sentiment analysis model offline
sentiment_analyzer = pipeline("sentiment-analysis", local_files_only=True)

# Load static AES key from file (generated securely during setup)
KEY_PATH = '/etc/personnel-system/aes_key.bin'
IV_PATH = '/etc/personnel-system/aes_iv.bin'

def load_key_iv():
    with open(KEY_PATH, 'rb') as f:
        key = f.read()
    with open(IV_PATH, 'rb') as f:
        iv = f.read()
    return key, iv

@app.route('/')
def home():
    return jsonify({
        "message": "Personnel Management System is operational and secure.",
        "features": [
            "AI-Powered Analytics (Offline)",
            "Encrypted Data Storage",
            "No Third-Party Services"
        ]
    })

@app.route('/analyze_employee_data', methods=['POST'])
def analyze_employee_data():
    try:
        payload = request.get_json(force=True)
        data = payload.get("employee_data", [])
        if not isinstance(data, list) or not data:
            raise ValueError("Invalid employee data format.")
        df = pd.DataFrame(data)
        analysis = df.describe().to_dict()
        return jsonify({"employee_analysis": analysis})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    try:
        payload = request.get_json(force=True)
        feedback = payload.get("feedback", "")
        if not isinstance(feedback, str) or not feedback:
            raise ValueError("No valid feedback provided.")
        analysis = sentiment_analyzer(feedback)
        return jsonify({"analysis": analysis})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/secure_employee_data', methods=['POST'])
def secure_employee_data():
    try:
        payload = request.get_json(force=True)
        data = payload.get("data", "")
        if not isinstance(data, str) or not data:
            raise ValueError("No valid data provided.")
        key, iv = load_key_iv()
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted = encryptor.update(data.encode()) + encryptor.finalize()
        return jsonify({"encrypted_data": encrypted.hex()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@socketio.on('broadcast_update')
def broadcast_update(data):
    if isinstance(data, dict):
        emit("receive_update", data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5006)

from flask import Flask, request, session, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash

app.secret_key = os.urandom(32)  # Should be static and stored securely in production

# Simulated user store (replace with secure file or DB later)
users = {
    "admin": {
        "password": generate_password_hash("adminpass"),
        "role": "admin"
    },
    "analyst": {
        "password": generate_password_hash("analystpass"),
        "role": "analyst"
    },
    "viewer": {
        "password": generate_password_hash("viewerpass"),
        "role": "viewer"
    }
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    username = request.form.get("username")
    password = request.form.get("password")
    if username in users and check_password_hash(users[username]["password"], password):
        session["username"] = username
        session["role"] = users[username]["role"]
        return redirect(url_for("dashboard"))
    return "Invalid credentials", 403

@app.route('/dashboard')
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", user_role=session.get("role"))

@app.route('/logout', methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login"))

from datetime import datetime

DATA_DIR = "/var/lib/personnel-system"
os.makedirs(DATA_DIR, exist_ok=True)

def save_encrypted_json(data, label="entry"):
    key, iv = load_key_iv()
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    serialized = json.dumps(data).encode()
    encrypted = encryptor.update(serialized) + encryptor.finalize()
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    filename = f"{label}_{timestamp}.bin"
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'wb') as f:
        f.write(encrypted)
    return filename

@app.route('/store_data', methods=['POST'])
def store_data():
    if session.get("role") != "admin":
        return "Forbidden", 403
    try:
        payload = request.get_json(force=True)
        filename = save_encrypted_json(payload)
        return jsonify({"message": "Data stored securely", "file": filename})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

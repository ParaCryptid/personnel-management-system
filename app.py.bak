
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from transformers import pipeline
import pandas as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

app = Flask(__name__)
socketio = SocketIO(app)

# Initialize AI models (e.g., NLP for sentiment analysis)
sentiment_analyzer = pipeline("sentiment-analysis")

@app.route('/')
def home():
    return jsonify({
        "message": "Personnel Management System repository is fully functional.",
        "features": [
            "AI-Powered Employee Analytics",
            "Real-Time Notifications",
            "Secure Data Handling"
        ]
    })

@app.route('/analyze_employee_data', methods=['POST'])
def analyze_employee_data():
    data = request.json.get("employee_data", [])
    if not data:
        return jsonify({"error": "No employee data provided"}), 400
    employee_df = pd.DataFrame(data)
    analysis = employee_df.describe().to_dict()
    return jsonify({"employee_analysis": analysis})

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.json.get("feedback", "")
    if not data:
        return jsonify({"error": "No feedback provided"}), 400
    analysis = sentiment_analyzer(data)
    return jsonify({"analysis": analysis})

@app.route('/secure_employee_data', methods=['POST'])
def secure_employee_data():
    data = request.json.get("data", "").encode()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    return jsonify({"encrypted_data": encrypted_data.hex(), "iv": iv.hex()})

@socketio.on('broadcast_update')
def broadcast_update(data):
    emit("receive_update", data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5006)

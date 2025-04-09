
# Personnel Management System

## Overview
The Personnel Management System has been enhanced with AI-powered analytics, real-time notifications, and secure data handling.

### New Features
1. **AI-Powered Employee Analytics**
    - Endpoint: `/analyze_employee_data`
    - Method: `POST`
    - Description: Analyzes employee data for insights and statistics.
    - Example Request:
      ```json
      {
          "employee_data": [
              {"name": "John", "age": 30, "department": "HR", "salary": 50000},
              {"name": "Jane", "age": 35, "department": "IT", "salary": 70000}
          ]
      }
      ```
    - Example Response:
      ```json
      {
          "employee_analysis": {...}
      }
      ```

2. **Sentiment Analysis**
    - Endpoint: `/analyze_sentiment`
    - Method: `POST`
    - Description: Analyzes employee feedback using AI for sentiment and insights.
    - Example Request:
      ```json
      {
          "feedback": "The new policies are very helpful and motivating."
      }
      ```
    - Example Response:
      ```json
      {
          "analysis": [{"label": "POSITIVE", "score": 0.95}]
      }
      ```

3. **Secure Data Handling**
    - Endpoint: `/secure_employee_data`
    - Method: `POST`
    - Description: Encrypts sensitive employee data for secure storage or transmission.
    - Example Request:
      ```json
      {
          "data": "Confidential employee information"
      }
      ```
    - Example Response:
      ```json
      {
          "encrypted_data": "abc123...",
          "iv": "456def..."
      }
      ```

4. **Real-Time Notifications**
    - Enables real-time updates and notifications using Flask-SocketIO.
    - Events:
      - `broadcast_update`: Send updates to all connected clients.
      - `receive_update`: Receive broadcasted updates.

### Getting Started
1. Install dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the application:
    ```bash
    python app.py
    ```

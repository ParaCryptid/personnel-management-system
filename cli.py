
import requests
import json
import getpass

BASE_URL = "http://127.0.0.1:5006"

session = requests.Session()

def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    resp = session.post(BASE_URL + "/login", data={"username": username, "password": password})
    if resp.ok:
        print("[+] Login successful.")
    else:
        print("[-] Login failed.")

def store_data():
    try:
        payload = json.loads(input("Enter JSON data to encrypt and store: "))
        resp = session.post(BASE_URL + "/store_data", json=payload)
        print(resp.json())
    except Exception as e:
        print(f"Error: {e}")

def analyze_sentiment():
    text = input("Enter text to analyze sentiment: ")
    resp = session.post(BASE_URL + "/analyze_sentiment", json={"feedback": text})
    print(resp.json())

def main():
    print("Secure Personnel CLI Client")
    login()
    while True:
        print("\nOptions: [1] Store Data  [2] Sentiment Analysis  [q] Quit")
        choice = input("Choose: ").strip()
        if choice == '1':
            store_data()
        elif choice == '2':
            analyze_sentiment()
        elif choice == 'q':
            break

if __name__ == "__main__":
    main()

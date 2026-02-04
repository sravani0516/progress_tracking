import requests
import threading
import time

BASE_URL = "http://127.0.0.1:8000"

name = input("Enter your name: ")

print(f"Welcome {name}!")
print("Type message and press Enter to send\n")

def receive_messages():
    seen = 0
    while True:
        try:
            res = requests.get(f"{BASE_URL}/messages")
            msgs = res.json()

            for msg in msgs[seen:]:
                print(f"{msg['user']}: {msg['text']}")
            seen = len(msgs)

            time.sleep(1)
        except:
            time.sleep(1)

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    text = input()
    data = {"user": name, "text": text}
    requests.post(f"{BASE_URL}/send", json=data)

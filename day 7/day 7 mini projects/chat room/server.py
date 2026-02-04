from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import threading

HOST = "127.0.0.1"
PORT = 8000

messages = []
lock = threading.Lock()

class ChatHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/messages":
            with lock:
                data = json.dumps(messages).encode()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(data)

    def do_POST(self):
        if self.path == "/send":
            length = int(self.headers["Content-Length"])
            body = self.rfile.read(length)
            msg = json.loads(body.decode())

            with lock:
                messages.append(msg)

            self.send_response(200)
            self.end_headers()

print("Server running on http://localhost:8000")
HTTPServer((HOST, PORT), ChatHandler).serve_forever()

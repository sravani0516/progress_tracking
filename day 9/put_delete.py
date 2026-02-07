from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import json

HOST = "localhost"
PORT = 8000

USERS = [
    {"id": 1, "name": "Sravani", "role": "student"},
    {"id": 2, "name": "Rahul", "role": "trainer"},
    {"id": 3, "name": "Anita", "role": "admin"}
]


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True


class SimpleAPI(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def parse_id(self):
        parts = self.path.strip("/").split("/")
        if len(parts) != 2 or parts[0] != "users":
            return None
        return parts[1]

    # ---------- GET ----------
    def do_GET(self):
        user_id = self.parse_id()

        if user_id is None:
            self.send_json(404, {"error": "Not found"})
            return

        if not user_id.isdigit():
            self.send_json(400, {"error": "Invalid user ID"})
            return

        user_id = int(user_id)

        for user in USERS:
            if user["id"] == user_id:
                self.send_json(200, user)
                return

        self.send_json(404, {"error": "User not found"})

    # ---------- PUT ----------
    def do_PUT(self):
        user_id = self.parse_id()

        if user_id is None:
            self.send_json(404, {"error": "Not found"})
            return

        if not user_id.isdigit():
            self.send_json(400, {"error": "Invalid user ID"})
            return

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self.send_json(400, {"error": "Invalid JSON"})
            return

        user_id = int(user_id)

        for user in USERS:
            if user["id"] == user_id:
                if "name" in data:
                    user["name"] = data["name"]
                if "role" in data:
                    user["role"] = data["role"]

                self.send_json(200, user)
                return

        self.send_json(404, {"error": "User not found"})

    # ---------- DELETE ----------
    def do_DELETE(self):
        user_id = self.parse_id()

        if user_id is None:
            self.send_json(404, {"error": "Not found"})
            return

        if not user_id.isdigit():
            self.send_json(400, {"error": "Invalid user ID"})
            return

        user_id = int(user_id)

        for i, user in enumerate(USERS):
            if user["id"] == user_id:
                deleted = USERS.pop(i)
                self.send_json(200, {"message": "User deleted", "user": deleted})
                return

        self.send_json(404, {"error": "User not found"})


def run():
    server = ThreadedHTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running at http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    run()

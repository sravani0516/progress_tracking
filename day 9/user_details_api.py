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

    def do_GET(self):
        path_parts = self.path.strip("/").split("/")

        # GET /users/{id}
        if len(path_parts) == 2 and path_parts[0] == "users":
            user_id = path_parts[1]

            # Invalid ID
            if not user_id.isdigit():
                self.send_json(400, {"error": "Invalid user ID"})
                return

            user_id = int(user_id)

            # Search user
            for user in USERS:
                if user["id"] == user_id:
                    self.send_json(200, user)
                    return

            # User not found
            self.send_json(404, {"error": "User not found"})
            return

        # Unknown route
        self.send_json(404, {"error": "Not found"})


def run():
    server = ThreadedHTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running at http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    run()

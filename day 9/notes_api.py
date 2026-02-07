from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import json

HOST = "localhost"
PORT = 8000

# In-memory storage
NOTES = []


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True


class NotesAPI(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        if self.path != "/notes":
            self.send_json(404, {"error": "Not found"})
            return

        content_length = int(self.headers.get("Content-Length", 0))
        raw_body = self.rfile.read(content_length)

        try:
            body = json.loads(raw_body)
        except json.JSONDecodeError:
            self.send_json(400, {"error": "Invalid JSON"})
            return

        # Validate required key
        if "text" not in body or not body["text"]:
            self.send_json(400, {"error": "Text is required"})
            return

        # Store note
        note = {"text": body["text"]}
        NOTES.append(note)

        self.send_json(201, note)

    def do_GET(self):
        if self.path == "/notes":
            self.send_json(200, NOTES)
            return

        self.send_json(404, {"error": "Not found"})


def run():
    server = ThreadedHTTPServer((HOST, PORT), NotesAPI)
    print(f"Server running at http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    run()

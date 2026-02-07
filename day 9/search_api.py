from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

# Sample product data
PRODUCTS = [
    {"id": 1, "name": "iPhone", "price": 700},
    {"id": 2, "name": "Android Phone", "price": 500},
    {"id": 3, "name": "Phone Case", "price": 100},
    {"id": 4, "name": "Laptop", "price": 1000}
]


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query = parse_qs(parsed_url.query)

        # /products endpoint
        if path == "/products":
            name = query.get("name", [""])[0].lower()
            max_price = query.get("max_price", [None])[0]

            result = []

            for product in PRODUCTS:
                # partial name match
                if name not in product["name"].lower():
                    continue

                # optional max_price filter
                if max_price is not None:
                    if product["price"] > int(max_price):
                        continue

                result.append(product)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())

        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode())


# Start server
server = HTTPServer(("localhost", 8000), MyHandler)
print("Server running at http://localhost:8000")
server.serve_forever()

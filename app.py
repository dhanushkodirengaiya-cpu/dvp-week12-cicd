
from http.server import BaseHTTPRequestHandler, HTTPServer


def get_message():
    return "DVP Week 12 CI/CD Pipeline is running!"


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = get_message()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), AppHandler)
    print("Application running on port 8000")
    server.serve_forever()

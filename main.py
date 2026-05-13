from http.server import HTTPServer, SimpleHTTPRequestHandler
import time
import os

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello from Python Lab 5!</h1>")
        print(f"[{time.strftime('%H:%M:%S')}] Request handled")

if __name__ == "__main__":
    port = 8080
    server = HTTPServer(('localhost', port), MyHandler)
    print(f"Starting server on port {port}...")
    print(f"Process ID (PID): {os.getpid()}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()


import http.server
import socketserver
from pathlib import Path

PORT = 8002
ROOT = Path(__file__).resolve().parent / "src"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

if __name__ == "__main__":
    with socketserver.TCPServer(("10.147.17.63", PORT), Handler) as httpd:
        print(f"Serving at http://10.147.17.63:{PORT}")
        httpd.serve_forever()
#!/usr/bin/env python3
"""
Simple HTTP server for CoSE MagBio-3D Interactive Report.
Usage:
    python3 serve.py [port]
    PORT=1234 python3 serve.py   # environment takes precedence
Default port: 8415
"""
import sys
import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT") or (sys.argv[1] if len(sys.argv) > 1 else 8415))
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"CoSE MagBio-3D Interactive Report running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

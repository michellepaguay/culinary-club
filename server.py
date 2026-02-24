#!/usr/bin/env python3
"""
Culinary Club Blog - Local Development Server
Run: python server.py
Then open: http://localhost:8080
"""

import http.server
import socketserver
import os
import webbrowser
from threading import Timer

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"  [{self.address_string()}] {format % args}")

def open_browser():
    webbrowser.open(f"http://localhost:{PORT}")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"\n🍴 Culinary Club Blog Server")
    print(f"   Running at: http://localhost:{PORT}")
    print(f"   Press Ctrl+C to stop\n")
    Timer(1.0, open_browser).start()
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n  Server stopped. See you next time! 👋\n")

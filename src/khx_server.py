#!/usr/bin/env python3
"""
KHX Server Module - HTTP Server and Networking Support
"""

import socket
import threading
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import time


class KHXHTTPHandler(BaseHTTPRequestHandler):
    """Custom HTTP request handler for KHX"""
    
    routes = {}
    
    def log_message(self, format, *args):
        """Override to customize logging"""
        print(f"[SERVER] {self.address_string()} - {format % args}")
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query = parse_qs(parsed_path.query)
        
        if path in self.routes:
            handler = self.routes[path]
            response = handler(path, query, {})
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404 Not Found</h1>')
    
    def do_POST(self):
        """Handle POST requests"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        try:
            data = json.loads(post_data.decode())
        except:
            data = {}
        
        if path in self.routes:
            handler = self.routes[path]
            response = handler(path, {}, data)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "data": response}).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "error", "message": "Not found"}).encode())


class KHXServer:
    """KHX HTTP Server"""
    
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.server = None
        self.thread = None
        self.running = False
        self.routes = {}
    
    def add_route(self, path, handler):
        """Add a route handler"""
        self.routes[path] = handler
        KHXHTTPHandler.routes[path] = handler
        print(f"[SERVER] Route added: {path}")
    
    def start(self):
        """Start the server"""
        if self.running:
            print("[SERVER] Server already running")
            return
        
        try:
            self.server = HTTPServer((self.host, self.port), KHXHTTPHandler)
            self.running = True
            
            print(f"[SERVER] Starting server on {self.host}:{self.port}")
            
            # Run in separate thread
            self.thread = threading.Thread(target=self._run_server)
            self.thread.daemon = True
            self.thread.start()
            
            print(f"[SERVER] Server running at http://{self.host}:{self.port}")
            return True
        except Exception as e:
            print(f"[SERVER] Error starting server: {e}")
            return False
    
    def _run_server(self):
        """Internal method to run server"""
        try:
            self.server.serve_forever()
        except Exception as e:
            print(f"[SERVER] Server error: {e}")
    
    def stop(self):
        """Stop the server"""
        if not self.running:
            print("[SERVER] Server not running")
            return
        
        print("[SERVER] Stopping server...")
        self.running = False
        if self.server:
            self.server.shutdown()
            self.server.server_close()
        print("[SERVER] Server stopped")
    
    def is_running(self):
        """Check if server is running"""
        return self.running


class KHXSocket:
    """Simple socket wrapper for KHX"""
    
    def __init__(self):
        self.socket = None
        self.connected = False
    
    def connect(self, host, port):
        """Connect to a server"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))
            self.connected = True
            print(f"[SOCKET] Connected to {host}:{port}")
            return True
        except Exception as e:
            print(f"[SOCKET] Connection error: {e}")
            return False
    
    def send(self, data):
        """Send data"""
        if not self.connected:
            print("[SOCKET] Not connected")
            return False
        
        try:
            self.socket.sendall(data.encode())
            return True
        except Exception as e:
            print(f"[SOCKET] Send error: {e}")
            return False
    
    def receive(self, buffer_size=1024):
        """Receive data"""
        if not self.connected:
            print("[SOCKET] Not connected")
            return ""
        
        try:
            data = self.socket.recv(buffer_size)
            return data.decode()
        except Exception as e:
            print(f"[SOCKET] Receive error: {e}")
            return ""
    
    def close(self):
        """Close connection"""
        if self.socket:
            self.socket.close()
            self.connected = False
            print("[SOCKET] Connection closed")


# Global server registry
_servers = {}
_server_counter = 0


def create_server(host='localhost', port=8080):
    """Create a new HTTP server"""
    global _server_counter
    server = KHXServer(host, port)
    server_id = f"server_{_server_counter}"
    _servers[server_id] = server
    _server_counter += 1
    return server_id


def get_server(server_id):
    """Get server by ID"""
    return _servers.get(server_id)


def start_server(server_id):
    """Start a server"""
    server = _servers.get(server_id)
    if server:
        return server.start()
    return False


def stop_server(server_id):
    """Stop a server"""
    server = _servers.get(server_id)
    if server:
        server.stop()
        return True
    return False


def add_route(server_id, path, handler):
    """Add route to server"""
    server = _servers.get(server_id)
    if server:
        server.add_route(path, handler)
        return True
    return False

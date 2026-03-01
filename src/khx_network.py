#!/usr/bin/env python3
"""
KHX Network Module - Advanced Networking
"""

import requests
import json
from urllib.parse import urljoin


class KHXRestClient:
    """REST API Client"""
    
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {}
        self.session = requests.Session()
    
    def set_header(self, key, value):
        """Set HTTP header"""
        self.headers[key] = value
    
    def get(self, endpoint, params=None):
        """GET request"""
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.get(url, headers=self.headers, params=params)
            return {
                "status": response.status_code,
                "body": response.text,
                "json": response.json() if response.headers.get('content-type', '').startswith('application/json') else None
            }
        except Exception as e:
            print(f"[HTTP] GET error: {e}")
            return {"status": 0, "body": str(e), "json": None}
    
    def post(self, endpoint, data=None, json_data=None):
        """POST request"""
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.post(url, headers=self.headers, data=data, json=json_data)
            return {
                "status": response.status_code,
                "body": response.text,
                "json": response.json() if response.headers.get('content-type', '').startswith('application/json') else None
            }
        except Exception as e:
            print(f"[HTTP] POST error: {e}")
            return {"status": 0, "body": str(e), "json": None}
    
    def put(self, endpoint, data=None, json_data=None):
        """PUT request"""
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.put(url, headers=self.headers, data=data, json=json_data)
            return {
                "status": response.status_code,
                "body": response.text,
                "json": response.json() if response.headers.get('content-type', '').startswith('application/json') else None
            }
        except Exception as e:
            print(f"[HTTP] PUT error: {e}")
            return {"status": 0, "body": str(e), "json": None}
    
    def delete(self, endpoint):
        """DELETE request"""
        url = urljoin(self.base_url, endpoint)
        try:
            response = self.session.delete(url, headers=self.headers)
            return {
                "status": response.status_code,
                "body": response.text,
                "json": response.json() if response.headers.get('content-type', '').startswith('application/json') else None
            }
        except Exception as e:
            print(f"[HTTP] DELETE error: {e}")
            return {"status": 0, "body": str(e), "json": None}


class KHXWebSocket:
    """WebSocket Client (Placeholder)"""
    
    def __init__(self, url):
        self.url = url
        self.connected = False
        print(f"[WebSocket] Created: {url}")
    
    def connect(self):
        """Connect to WebSocket"""
        self.connected = True
        print(f"[WebSocket] Connected to {self.url}")
        return True
    
    def send(self, message):
        """Send message"""
        if self.connected:
            print(f"[WebSocket] Sent: {message}")
            return True
        return False
    
    def close(self):
        """Close connection"""
        self.connected = False
        print("[WebSocket] Closed")


# Global registry
_rest_clients = {}
_websockets = {}
_client_counter = 0
_ws_counter = 0


def create_rest_client(base_url):
    """Create REST client"""
    global _client_counter
    client = KHXRestClient(base_url)
    client_id = f"rest_{_client_counter}"
    _rest_clients[client_id] = client
    _client_counter += 1
    return client_id


def get_rest_client(client_id):
    """Get REST client"""
    return _rest_clients.get(client_id)


def create_websocket(url):
    """Create WebSocket"""
    global _ws_counter
    ws = KHXWebSocket(url)
    ws_id = f"ws_{_ws_counter}"
    _websockets[ws_id] = ws
    _ws_counter += 1
    return ws_id


def get_websocket(ws_id):
    """Get WebSocket"""
    return _websockets.get(ws_id)

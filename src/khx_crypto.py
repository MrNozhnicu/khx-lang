#!/usr/bin/env python3
"""
KHX Cryptography Module
"""

import hashlib
import base64
import secrets
import hmac
from datetime import datetime, timedelta


class KHXCrypto:
    """Cryptography utilities"""
    
    @staticmethod
    def sha256(text):
        """SHA-256 hash"""
        return hashlib.sha256(text.encode()).hexdigest()
    
    @staticmethod
    def md5(text):
        """MD5 hash"""
        return hashlib.md5(text.encode()).hexdigest()
    
    @staticmethod
    def sha512(text):
        """SHA-512 hash"""
        return hashlib.sha512(text.encode()).hexdigest()
    
    @staticmethod
    def base64_encode(text):
        """Base64 encode"""
        return base64.b64encode(text.encode()).decode()
    
    @staticmethod
    def base64_decode(text):
        """Base64 decode"""
        return base64.b64decode(text.encode()).decode()
    
    @staticmethod
    def generate_token(length=32):
        """Generate random token"""
        return secrets.token_hex(length)
    
    @staticmethod
    def generate_password(length=16):
        """Generate random password"""
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        return ''.join(secrets.choice(alphabet) for _ in range(length))
    
    @staticmethod
    def hmac_sha256(message, key):
        """HMAC-SHA256"""
        return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()


class KHXJWT:
    """JWT Token Handler"""
    
    @staticmethod
    def create(payload, secret, expiry_hours=24):
        """Create JWT token (simplified)"""
        import json
        
        # Header
        header = {"alg": "HS256", "typ": "JWT"}
        header_encoded = base64.b64encode(json.dumps(header).encode()).decode()
        
        # Payload with expiry
        payload["exp"] = (datetime.now() + timedelta(hours=expiry_hours)).timestamp()
        payload_encoded = base64.b64encode(json.dumps(payload).encode()).decode()
        
        # Signature
        message = f"{header_encoded}.{payload_encoded}"
        signature = hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest()
        
        token = f"{header_encoded}.{payload_encoded}.{signature}"
        print(f"[JWT] Token created (expires in {expiry_hours}h)")
        return token
    
    @staticmethod
    def verify(token, secret):
        """Verify JWT token"""
        try:
            parts = token.split('.')
            if len(parts) != 3:
                return False
            
            header_encoded, payload_encoded, signature = parts
            
            # Verify signature
            message = f"{header_encoded}.{payload_encoded}"
            expected_signature = hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest()
            
            if signature != expected_signature:
                print("[JWT] Invalid signature")
                return False
            
            # Check expiry
            import json
            payload = json.loads(base64.b64decode(payload_encoded).decode())
            if "exp" in payload:
                if datetime.now().timestamp() > payload["exp"]:
                    print("[JWT] Token expired")
                    return False
            
            print("[JWT] Token valid")
            return True
        except Exception as e:
            print(f"[JWT] Verification error: {e}")
            return False
    
    @staticmethod
    def decode(token):
        """Decode JWT payload"""
        try:
            import json
            parts = token.split('.')
            if len(parts) != 3:
                return None
            payload_encoded = parts[1]
            payload = json.loads(base64.b64decode(payload_encoded).decode())
            return payload
        except Exception as e:
            print(f"[JWT] Decode error: {e}")
            return None


class KHXPassword:
    """Password utilities"""
    
    @staticmethod
    def hash(password, salt=None):
        """Hash password (simplified bcrypt-like)"""
        if salt is None:
            salt = secrets.token_hex(16)
        
        hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
        return f"{salt}${hashed.hex()}"
    
    @staticmethod
    def verify(password, hashed):
        """Verify password"""
        try:
            salt, hash_value = hashed.split('$')
            new_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
            return new_hash.hex() == hash_value
        except:
            return False


# Export functions
def sha256(text):
    return KHXCrypto.sha256(text)

def md5(text):
    return KHXCrypto.md5(text)

def base64_encode(text):
    return KHXCrypto.base64_encode(text)

def base64_decode(text):
    return KHXCrypto.base64_decode(text)

def generate_token(length=32):
    return KHXCrypto.generate_token(length)

def create_jwt(payload, secret, expiry_hours=24):
    return KHXJWT.create(payload, secret, expiry_hours)

def verify_jwt(token, secret):
    return KHXJWT.verify(token, secret)

def hash_password(password):
    return KHXPassword.hash(password)

def verify_password(password, hashed):
    return KHXPassword.verify(password, hashed)

# game/core/security.py
import hashlib
import os
from cryptography.fernet import Fernet

class SecurityManager:
    def __init__(self):
        self.key = os.getenv("ENCRYPTION_KEY").encode()
        self.cipher = Fernet(self.key)
        
    def hash_password(self, password: str) -> str:
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(
            'sha512',
            password.encode(),
            salt,
            100000
        )
        return f"{salt.hex()}:{key.hex()}"
        
    def encrypt_data(self, data: str) -> str:
        return self.cipher.encrypt(data.encode()).decode()
        
    def decrypt_data(self, encrypted: str) -> str:
        return self.cipher.decrypt(encrypted.encode()).decode()
import os
import base58
from solana.keypair import Keypair
from solana.rpc.api import Client
from cryptography.fernet import Fernet

class WalletManager:
    def __init__(self):
        self.client = Client(os.getenv("SOLANA_RPC_URL"))
        self.cipher = Fernet(os.getenv("ENCRYPTION_KEY"))
        
    def generate_wallet(self) -> tuple:
        kp = Keypair()
        encrypted = self.cipher.encrypt(kp.secret_key)
        return str(kp.public_key), base58.b58encode(encrypted).decode()
        
    def validate_transaction(self, tx_signature: str) -> bool:
        return self.client.get_confirmed_transaction(tx_signature) is not None
        
    def decrypt_wallet(self, encrypted_key: str) -> Keypair:
        decrypted = self.cipher.decrypt(base58.b58decode(encrypted_key))
        return Keypair.from_secret_key(decrypted)
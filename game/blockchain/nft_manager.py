from solana.rpc.api import Client
from solana.keypair import Keypair
from solders.system_program import TransferParams, transfer
from cryptography.fernet import Fernet

class NFTManager:
    def __init__(self):
        self.client = Client(os.getenv("SOLANA_RPC_URL"))
        self.cipher = Fernet(os.getenv("ENCRYPTION_KEY"))
        
    def decrypt_wallet(self):
        seed = self.cipher.decrypt(os.getenv("WALLET_SEED").encode())
        return Keypair.from_secret_key(seed)
        
    def mint_item(self, receiver: str, metadata: dict):
        wallet = self.decrypt_wallet()
        txn = Transaction().add(
            transfer(
                TransferParams(
                    from_pubkey=wallet.pubkey(),
                    to_pubkey=receiver,
                    lamports=int(metadata['value'] * 1e9)
                )
            )
        )
        return self.client.send_transaction(txn, wallet)
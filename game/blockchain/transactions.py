from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from solders.signature import Signature

class TransactionManager:
    def __init__(self, wallet_manager):
        self.wallet_manager = wallet_manager
        
    def send_funds(self, sender_encrypted: str, receiver: str, amount: float) -> Signature:
        sender_kp = self.wallet_manager.decrypt_wallet(sender_encrypted)
        txn = Transaction().add(
            transfer(
                TransferParams(
                    from_pubkey=sender_kp.public_key,
                    to_pubkey=receiver,
                    lamports=int(amount * 1e9)
                )
            )
        )
        return self.wallet_manager.client.send_transaction(txn, sender_kp)
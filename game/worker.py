# game/worker.py
import time
import redis
from game.blockchain import transactions

r = redis.Redis.from_url(os.getenv("REDIS_URL"))
tx_manager = transactions.TransactionManager()

def process_transactions():
    while True:
        _, task = r.blpop('transactions')
        try:
            data = json.loads(task)
            if data['type'] == 'nft_mint':
                result = tx_manager.mint_item(
                    data['receiver'],
                    data['metadata']
                )
                r.rpush('completed_tx', result.value)
        except Exception as e:
            r.rpush('failed_tx', str(e))

if __name__ == "__main__":
    process_transactions()
    
    
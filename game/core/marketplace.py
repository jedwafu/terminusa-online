import time
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class MarketListing:
    item_id: str
    seller: str
    price: float
    currency: str
    listed_at: float = time.time()
    expires_at: float = time.time() + 604800  # 1 week

class Marketplace:
    def __init__(self):
        self.listings: List[MarketListing] = []
        self.transaction_history: List[Dict] = []
        
    def list_item(self, item: dict, seller: str, price: float, currency: str) -> str:
        listing = MarketListing(
            item_id=item['name'] + str(time.time()),
            seller=seller,
            price=price,
            currency=currency
        )
        self.listings.append(listing)
        return listing.item_id
        
    def buy_item(self, buyer: object, item_id: str) -> bool:
        listing = next((l for l in self.listings if l.item_id == item_id), None)
        if not listing:
            return False
            
        if getattr(buyer.currency, listing.currency) < listing.price:
            return False
            
        # Process transaction with tax
        tax = listing.price * 0.05
        total_cost = listing.price + tax
        
        # Deduct funds
        setattr(buyer.currency, listing.currency, 
               getattr(buyer.currency, listing.currency) - total_cost)
        
        # Record transaction
        self.transaction_history.append({
            'item': item_id,
            'buyer': buyer.name,
            'seller': listing.seller,
            'price': listing.price,
            'tax': tax,
            'timestamp': time.time()
        })
        
        # Add item to buyer inventory
        buyer.inventory.append(item_id)
        self.listings.remove(listing)
        return True
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Player:
    name: str
    level: int = 1
    exp: int = 0
    stats: Dict[str, int] = None
    inventory: List[str] = None
    wallet: str = None
    current_hp: int = 100
    
    def __post_init__(self):
        self.stats = {
            'str': 10, 'agi': 10, 'vit': 10, 
            'int': 10, 'luk': 10
        }
        self.inventory = []
        self.max_hp = 100 + (self.stats['vit'] * 5)
        
    def level_up(self):
        self.level += 1
        self.stats = {k: v+1 for k, v in self.stats.items()}
        self.max_hp = 100 + (self.stats['vit'] * 5)
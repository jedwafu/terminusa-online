import random
from enum import Enum
from typing import Dict

class ItemRarity(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5
    MYTHIC = 6

class LootGenerator:
    def __init__(self, dungeon_class: str):
        self.rarity_weights = self._get_rarity_weights(dungeon_class)
        self.prefixes = {
            ItemRarity.COMMON: ['Rusty', 'Old', 'Worn'],
            ItemRarity.UNCOMMON: ['Polished', 'Sharp', 'Sturdy'],
            ItemRarity.RARE: ['Enchanted', 'Gilded', 'Tempered'],
            ItemRarity.EPIC: ['Dragonforged', 'Ethereal', 'Celestial'],
            ItemRarity.LEGENDARY: ['Annihilating', 'Omniscient', 'Eternal'],
            ItemRarity.MYTHIC: ['Primordial', 'Cosmic', 'Transcendent']
        }
        self.item_types = ['Sword', 'Shield', 'Amulet', 'Ring', 'Armor']
        
    def _get_rarity_weights(self, dungeon_class: str) -> Dict[ItemRarity, float]:
        weights = {
            'S': [0.05, 0.10, 0.20, 0.30, 0.25, 0.10],
            'A': [0.10, 0.20, 0.30, 0.25, 0.10, 0.05],
            'B': [0.20, 0.30, 0.35, 0.10, 0.04, 0.01],
            'C': [0.30, 0.40, 0.25, 0.04, 0.01, 0.00],
            'D': [0.40, 0.45, 0.14, 0.01, 0.00, 0.00],
            'E': [0.50, 0.45, 0.05, 0.00, 0.00, 0.00]
        }
        return {ItemRarity(i+1): weight for i, weight in enumerate(weights[dungeon_class])}
        
    def generate_item(self, player_luck: int) -> dict:
        rarity = random.choices(
            list(ItemRarity),
            weights=list(self.rarity_weights.values())
        )[0]
        
        return {
            'name': f"{random.choice(self.prefixes[rarity])} {random.choice(self.item_types)}",
            'rarity': rarity,
            'stats': self._generate_stats(rarity, player_luck),
            'nft_metadata': self._generate_nft_metadata()
        }
        
    def _generate_stats(self, rarity: ItemRarity, luck: int) -> dict:
        return {
            'attack': random.randint(5, 10) * rarity.value,
            'defense': random.randint(3, 7) * rarity.value,
            'luck': luck // 2
        }
        
    def _generate_nft_metadata(self) -> dict:
        return {
            'attributes': [
                {'trait_type': 'generated', 'value': 'true'},
                {'trait_type': 'game_version', 'value': '1.0'}
            ]
        }
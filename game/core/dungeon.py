import random
from enum import Enum
from dataclasses import dataclass
from .loot import LootGenerator

class DungeonClass(Enum):
    E = 1
    D = 2
    C = 3
    B = 4
    A = 5
    S = 6

@dataclass
class Monster:
    name: str
    level: int
    stats: dict
    hp: int

class Dungeon:
    def __init__(self, dungeon_class: DungeonClass):
        self.class_ = dungeon_class
        self.monsters = self.generate_monsters()
        self.loot_generator = LootGenerator(dungeon_class.name)
        
    def generate_monsters(self) -> list[Monster]:
        monsters = []
        base_level = self.class_.value * 5
        for i in range(3):
            monsters.append(Monster(
                name=f"{self.class_.name}-Monster-{i+1}",
                level=base_level + i,
                stats={
                    'str': random.randint(8, 12) * self.class_.value,
                    'vit': random.randint(5, 8) * self.class_.value,
                    'luk': random.randint(1, 3) * self.class_.value
                },
                hp=100 * self.class_.value
            ))
        return monsters
        
    def generate_loot(self, player_luck: int) -> dict:
        return self.loot_generator.generate_item(player_luck)
import random
from enum import Enum

class CombatResult(Enum):
    WIN = 1
    LOSE = 2
    FLEE = 3

class CombatEngine:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        
    def attack_roll(self, attacker, defender):
        base_dmg = attacker['str'] * 2 - defender['vit']
        crit_chance = attacker['luk'] / 1000
        return base_dmg * (2 if random.random() < crit_chance else 1)
        
    def resolve_combat(self):
        while self.player.current_hp > 0 and self.monster.hp > 0:
            # Player turn
            monster_dmg = self.attack_roll(self.player.stats, self.monster)
            self.monster.hp -= monster_dmg
            
            # Monster turn
            player_dmg = self.attack_roll(self.monster.stats, self.player)
            self.player.current_hp -= player_dmg
            
        return CombatResult.WIN if self.player.current_hp > 0 else CombatResult.LOSE
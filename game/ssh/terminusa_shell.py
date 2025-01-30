# game/ssh/terminusa_shell.py
import sys
import cmd
from game.core.player import Player
from game.core.dungeon import Dungeon, DungeonClass
from game.core.combat import CombatEngine, CombatResult

class TerminusaShell(cmd.Cmd):
    prompt = 'Terminusa> '
    
    def __init__(self, stdin, stdout):
        super().__init__(stdin=stdin, stdout=stdout)
        self.player = None
        self.current_dungeon = None
        
    def start(self):
        self.stdout.write("Terminusa Online - SSH Interface\n")
        self.authenticate()
        self.cmdloop()
        
    def authenticate(self):
        self.stdout.write("Username: ")
        username = sys.stdin.readline().strip()
        self.player = Player(name=username)
        
    def do_enter(self, arg):
        """Enter a dungeon: enter <class>"""
        try:
            dungeon_class = DungeonClass[arg.upper()]
            self.current_dungeon = Dungeon(dungeon_class)
            self.stdout.write(f"Entered {dungeon_class.name} dungeon!\n")
        except KeyError:
            self.stdout.write("Invalid dungeon class (E-S)\n")
            
    def do_attack(self, arg):
        if not self.current_dungeon:
            self.stdout.write("Not in a dungeon!\n")
            return
            
        combat = CombatEngine(self.player, self.current_dungeon.monsters[0])
        result = combat.resolve_combat()
        
        if result == CombatResult.WIN:
            self.stdout.write("You defeated the monster!\n")
        else:
            self.stdout.write("You were defeated!\n")
            
    def do_exit(self, arg):
        self.stdout.write("Logging out...\n")
        return True

if __name__ == "__main__":
    shell = TerminusaShell(sys.stdin, sys.stdout)
    shell.start()
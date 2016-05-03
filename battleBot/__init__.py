from battleBot.Movement import Movement
from battleBot.Weapon import Weapon


class BattleBot:
    def __init__(self):
        print("Battle Bot Constructor")
        self.movement = Movement()
        self.weapon = Weapon()

    def move_forward(self, direction, speed):
        self.movement.move(direction, speed)

    def attack(self):
        self.weapon.attack()

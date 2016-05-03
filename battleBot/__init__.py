from battleBot.Movement import Movement


class BattleBot:
    def __init__(self):
        print("Battle Bot Constructor")
        self.movement = Movement()

    def moveForward(self, direction, speed, ):
        Movement.move(self.movement, direction, speed)

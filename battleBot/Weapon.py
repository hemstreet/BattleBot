class Weapon:
    is_reset = True
    is_active = False

    def __init__(self):
        print("Weapon Constructor")

    def attack(self):

        # Avoid activating weapon twice, lets check to see if it is active
        if not self.is_active:

            # Set weapon status to active
            self.is_active = True
            # Set the weapon reset status to False to know it's not in a position to fire again until reset is called
            self.is_reset = False

            print("Weapon not active, do weapon things")

            # Reset the weapon
            self.reset()
        else:
            print("Weapon active")

    def reset(self):

        print('Resetting weapon back to origin state')
        self.is_reset = True

        # Set weapon status back to false
        self.is_active = False

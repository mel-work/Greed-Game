import random

class Turn:
    dice_max = 6
    min_min = 1
    dice_held = 0
    dice_left = 6

    def __init__(self):
        self.quantity = 6

    def roll(self, quantity=6):
        random_rolls = [[random.randint(1, 6)] for x in range(quantity)]
        return random_rolls

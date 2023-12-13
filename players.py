import random

class Player:
    def __init__(self, player):
        self.name = player
        self.is_turn = False
        self.total_score = 0
        self.turn_score = 0
        self.round_score = 0 
        self.dice_held = 0
        self.dice_to_roll = 6

    def __repr__(self) -> str:
        return self.name
    
    def roll(self, quantity=6):
        random_rolls = [[random.randint(1, 6)] for x in range(quantity)]
        return random_rolls
    
    def hold_and_roll(self, n_held, d_held):
        # Update quantities
        self.dice_held = n_held
        n_to_roll = self.dice_to_roll - n_held
        self.dice_to_roll = n_to_roll

        # get score from held (d_held = list of held dice)
        # update self.turn_score




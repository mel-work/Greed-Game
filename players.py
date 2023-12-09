

class Player:
    def __init__(self, player):
        self.name = player
        self.is_turn = False
        self.total_score = 0
        self.turn_score = 0
        self.round_score = 0 

    def __repr__(self) -> str:
        return self.name


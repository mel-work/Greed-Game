from players import Player

class Game:
    def __init__(self, playerList):
        players = [Player(player) for player in playerList]
    
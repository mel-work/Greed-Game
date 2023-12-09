from players import Player
import random
import discord
from discord.ui import Button, View
from turn import Turn
import functions


class Game:
    def __init__(self, playerList, interaction):
        self.players = [Player(player) for player in playerList]
        self.highest_score = 0
        self.interaction = interaction

    def __repr__(self) -> str:
        return (", ").join(self.players)

    async def start_game(self):
        # Game Loop
        while self.highest_score < 10000:
            for player in self.players:
                player.is_turn = True
                while player.is_turn:
                    await functions.turn_intro(self.interaction, player)
                    break
                break
            break


    def check_score(self, held):
        sorted_roll = sorted(held, key=lambda x: x[0])
        print(sorted_roll)
            


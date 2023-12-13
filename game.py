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


    def check_score(self, held):
        sorted_roll = sorted(held, key=lambda x: x[0])
        print(sorted_roll)

    async def begin_game(self):
    # While the highest score is < 10000,
        while self.highest_score < 10000:
    #   Loop through the players list,
            for player in self.players:
    #     While player turn,
                player.is_turn = True
                while player.is_turn:
                    await functions.turn_intro(self.interaction, player)
                    break
                break
            break
    #         Player begins turn with 6 dice
    #           They roll `n` dice
                    

 
    #             Case 1: Hold and roll
    #                 Remove held dice,
    #                 Update Score,
    #                 Update dice to roll
    #                 continue loop
    #             Case 2: Hold and Stay
    #                 Remove held dice,
    #                 Update turn score
    #                 Update player score
    #                 player.is_turn = False
    #             Bust
    #                 Remove all points gained this round
    #                 player.is_turn = False
            


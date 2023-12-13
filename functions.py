import calendar
import datetime
from discord.ui import Button, View
import discord
from app import client
from game import Game
from players import Player
from itertools import chain

roll_button = Button(style=discord.ButtonStyle.success, label='Roll')
stay_button = Button(style=discord.ButtonStyle.blurple, label="Stay")  

def getUnix():
    """Returns the Unix timestamp for 60 seconds from the time it was created."""
    future = datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
    return future, calendar.timegm(future.timetuple())  


async def game_intro(ctx):
    orig_user = ctx.user.display_name
    # end_time, time = getUnix()
    player_list = [orig_user]

    embed = discord.Embed(title=f'Let\'s Play Greed!', description='Press the button below to join!', color=0x00ff00)
    embed.add_field(name='Players Joined', value=('\n').join(player_list), inline=False)
    join = Button(style=discord.ButtonStyle.blurple, label='Join Game!')
    how_to_play = Button(style=discord.ButtonStyle.green, label='How to Play', url="https://thehobbyts.com/greed-dice-game-rules/")
    start = Button(style=discord.ButtonStyle.success, label="Start")
    leave = Button(style=discord.ButtonStyle.danger, label='Leave')
    view = View()
    view.add_item(join)
    view.add_item(how_to_play)
    view.add_item(leave)
    view.add_item(start)

    
    await ctx.response.send_message(content=f"{ctx.user.mention} started a game of Greed", embed=embed, view=view)
    

    async def join_callback(interaction):
        user = interaction.user.display_name
        if user not in player_list:
            player_list.append(user)
            updated_embed = discord.Embed(title=f'Let\'s Play Greed!', description='Press the button below to join!', color=0x00ff00).add_field(name='Players Joined', value=('\n').join(player_list), inline=False)
            await interaction.message.edit(embed=updated_embed)
            await interaction.response.defer()
        else:
            await interaction.response.send_message(content="You are already playing the game!", ephemeral=True)
        
        

    async def leave_callback(interaction):
        user = interaction.user.display_name
        if user not in player_list:
            await interaction.response.send_message(content="You are not currently playing.", ephemeral=True)
        else:
            if orig_user == user:
                await interaction.response.send_message(content="You cannot leave the game you started!", ephemeral=True)
            else:
                player_list.remove(user)
                updated_embed = discord.Embed(title=f'Let\'s Play Greed!', description='Press the button below to join!', color=0x00ff00).add_field(name='Players Joined', value=('\n').join(player_list), inline=False)
                await interaction.message.edit(embed=updated_embed, view=view)
                await interaction.response.defer()

        
    async def start_callback(interaction):
        updated_embed = discord.Embed(title=f'Time to Play!')
        await interaction.message.edit(embed=updated_embed)
        await interaction.response.defer()
        # await interaction.response.send_message(content="Starting Game!", ephemeral=True)
        game = Game(player_list, interaction)
        await game.begin_game()


    join.callback = join_callback
    leave.callback = leave_callback
    start.callback = start_callback
    
async def turn_intro(interaction, player):
    print("Turn Intro Function Ran!")
    updated_embed = discord.Embed(title=f'{player.name}\'s Turn!', color=0x00ff00)
    await interaction.message.edit(content='',embed=updated_embed, view=View().add_item(roll_button))

    async def roll_callback(interaction):
        if interaction.user.display_name == player.name:
            roll_result = player.roll(player.dice_to_roll)
            await interaction.response.defer()
            await result(interaction, player, roll_result)
        else:
            await interaction.response.send_message(content="It's not your turn yet.", ephemeral=True)

    async def stay_callback(interaction):
        if interaction.user.display_name == player.name:
            player.is_turn = False
            print(f"{player.name} ended turn")
            await interaction.response.defer()
        else:
            await interaction.response.send_message(content="It's not your turn.", ephemeral=True)


    roll_button.callback = roll_callback
    stay_button.callback = stay_callback

async def result(interaction, player, roll_result):
    print("Result Function Ran!")
    view = View()
    d1 = Button(style=discord.ButtonStyle.blurple, label=str(roll_result[0]))
    d2 = Button(style=discord.ButtonStyle.blurple, label=str(roll_result[1]))
    d3 = Button(style=discord.ButtonStyle.blurple, label=str(roll_result[2]))
    d4 = Button(style=discord.ButtonStyle.blurple, label=str(roll_result[3]))
    d5 = Button(style=discord.ButtonStyle.blurple, label=str(roll_result[4]))
    d6 = Button(style=discord.ButtonStyle.blurple, label=str(roll_result[5]))
    buttons = [d1, d2, d3, d4, d5, d6, roll_button, stay_button]
    for button in buttons:
        view.add_item(button)
    updated_embed = discord.Embed(title=f'{player.name} Rolled!', description= "Select which dice to hold", color=0x00ff00).add_field(
        name="Turn Score", value=f"{player.turn_score}")
    await interaction.message.edit(embed=updated_embed, view=view)

    async def hold_callback1(interaction):
        d2.disabled = True
        await interaction.response.defer()

    async def hold_callback2(interaction):
        d2.disabled = True
        await interaction.response.defer()

    async def hold_callback3(interaction):
        d3.disabled = True
        await interaction.response.defer()

    async def hold_callback4(interaction):
        d4.disabled = True
        await interaction.response.defer()

    async def hold_callback5(interaction):
        d5.disabled = True
        await interaction.response.defer()
    
    async def hold_callback6(interaction):
        d6.disabled = True
        await interaction.response.defer()

    d1.callback = hold_callback1
    d2.callback = hold_callback2
    d3.callback = hold_callback3
    d4.callback = hold_callback4
    d5.callback = hold_callback5
    d6.callback = hold_callback6


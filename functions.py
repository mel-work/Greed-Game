import calendar
import datetime
from discord.ui import Button, View
import discord
from app import client
from game import Game
from turn import Turn
from itertools import chain

roll_button = Button(style=discord.ButtonStyle.success, label='Roll')

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
        await game.start_game()


    join.callback = join_callback
    leave.callback = leave_callback
    start.callback = start_callback
    
async def turn_intro(interaction, player):
    updated_embed = discord.Embed(title=f'{player.name}\'s Turn!', color=0x00ff00)
    turn = Turn()
    await interaction.message.edit(content='',embed=updated_embed, view=View().add_item(roll_button))

    async def roll_callback(interaction):
        if interaction.user.display_name == player.name:
            roll = turn.roll()
            await follow_up_turn(interaction, roll, player)
            await interaction.response.defer()
        else:
            await interaction.response.send_message(content="It's not your turn yet.", ephemeral=True)

    roll_button.callback = roll_callback

async def follow_up_turn(interaction, roll, player):
    view = View()
    buttons = [roll_button]
    for dice in enumerate(roll):
        button = Button(style=discord.ButtonStyle.blurple, label=str(dice[1]))
        buttons.append(button)
    for button in buttons:
        view.add_item(button)
    updated_embed = discord.Embed(title=f'{player.name} Rolled!', description= "Select which dice to hold", color=0x00ff00).add_field(
        name="Turn Score", value=f"{player.turn_score}")
    await interaction.message.edit(embed=updated_embed, view=view)

    
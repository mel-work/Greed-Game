import calendar
import datetime
from discord.ui import Button, View
import discord
from app import client

def getUnix():
    """Returns the Unix timestamp for 60 seconds from the time it was created."""
    future = datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
    return calendar.timegm(future.timetuple())  


async def game_intro(ctx):
    orig_user = ctx.user.display_name
    player_list = [orig_user]
    timestamp = getUnix()

    embed = discord.Embed(title=f'Game Starting... <t:{timestamp}:R>', description='Press the button below to join!', color=0x00ff00)
    embed.add_field(name='Players Joined', value=('\n').join(player_list), inline=False)
    join = Button(style=discord.ButtonStyle.blurple, label='Join Game!')
    how_to_play = Button(style=discord.ButtonStyle.green, label='How to Play', url="https://thehobbyts.com/greed-dice-game-rules/")
    leave = Button(style=discord.ButtonStyle.danger, label='Leave Game')
    view = View()
    view.add_item(join)
    view.add_item(how_to_play)
    view.add_item(leave)


    async def join_callback(interaction):
        user = interaction.user.display_name
        if user not in player_list:
            player_list.append(user)
            updated_embed = discord.Embed(title=f'Game Starting... <t:{timestamp}:R>', description='Press the button below to join!', color=0x00ff00).add_field(name='Players Joined', value=('\n').join(player_list), inline=False)
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
                updated_embed = discord.Embed(title=f'Game Starting... <t:{timestamp}:R>', description='Press the button below to join!', color=0x00ff00).add_field(name='Players Joined', value=('\n').join(player_list), inline=False)
                await interaction.message.edit(embed=updated_embed, view=view)
                await interaction.response.defer()

    join.callback = join_callback
    leave.callback = leave_callback
    msg = await ctx.response.send_message(content=f"{ctx.user.mention} started a game of Greed", embed=embed, view=view)
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
    timestamp = getUnix()

    embed = discord.Embed(title=f'Game Starting... <t:{timestamp}:R>', description='Press the button below to join!', color=0x00ff00)
    embed.add_field(name='Players Joined', value=f'{ctx.user.display_name}\nTest\nTest2', inline=False)
    join = Button(style=discord.ButtonStyle.blurple, label='Join Game!')
    how_to_play = Button(style=discord.ButtonStyle.green, label='How to Play', url="https://thehobbyts.com/greed-dice-game-rules/")
    leave = Button(style=discord.ButtonStyle.danger, label='Leave Game')
    view = View()
    view.add_item(join)
    view.add_item(how_to_play)
    view.add_item(leave)

    async def join_callback(interaction):
        await interaction.response.send_message("Join Pressed!")
        # update players on embed

    async def leave_callback(interaction):
        await interaction.response.send_message("Leave Pressed!")
        # update players on embed

    join.callback = join_callback
    leave.callback = leave_callback
    await ctx.response.send_message(content=f"{ctx.user.mention} started a game of Greed", embed=embed, view=view)
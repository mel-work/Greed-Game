from dotenv import load_dotenv
from dotenv import dotenv_values
import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands
from discord.ui import Button, View
import functions

# Secret Connection
load_dotenv()
config = dotenv_values(".env")

# Intents Connection
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# App connection
client = commands.Bot(command_prefix="/", intents=discord.Intents.all())
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# Commands
@client.tree.command(name="start_game", description="Begin a new game!")
async def start_game(interaction: discord.Interaction):

    timestamp = functions.getUnix()

    embed = discord.Embed(title=f'Game Starting... <t:{timestamp}:R>', description='Press the button below to join!', color=0x00ff00)
    embed.add_field(name='Players Joined', value=f'{interaction.user.display_name}\nTest\nTest2', inline=False)
    join = Button(style=discord.ButtonStyle.blurple, label='Join Game!')
    how_to_play = Button(style=discord.ButtonStyle.green, label='How to Play', url="https://thehobbyts.com/greed-dice-game-rules/")
    leave_game = Button(style=discord.ButtonStyle.danger, label='Leave Game')
    view = View()
    view.add_item(join)
    view.add_item(how_to_play)
    view.add_item(leave_game)

    await interaction.response.send_message(content=f"{interaction.user.mention} started a game of Greed", embed=embed, view=view)


if __name__ == "__main__":
    client.run(config["APP_TOKEN"])
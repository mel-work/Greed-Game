from dotenv import load_dotenv
from dotenv import dotenv_values
import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
# from game import Game
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
    # Cronjob 60 seconds - 
    await functions.game_intro(interaction)

    # Begin Game
    # game = Game()



if __name__ == "__main__":
    client.run(config["APP_TOKEN"])
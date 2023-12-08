from dotenv import load_dotenv
from dotenv import dotenv_values
import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands

# Secret Connection
load_dotenv()
config = dotenv_values(".env")

# Intents Connection
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# Test Commands
@client.tree.command(name="test")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message(f"I'm working as intended, {interaction.user.mention}!",
                                            ephemeral=True)

@client.tree.command(name="say")
@app_commands.describe(what_to_say = "What should I say?")
async def say(interaction: discord.Interaction, what_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said {what_to_say}")

if __name__ == "__main__":
    client.run(config["APP_TOKEN"])
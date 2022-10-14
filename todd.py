import os
import discord
from discord.ext import commands


token = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=['<@!1026624616552218684> ', '<@1026624616552218684> '], intents=intents)


# Once the bot is ready, load cogs (commands)
# and print a message to verify connection
@client.event
async def on_ready():
    await load_cogs()
    print(f"{client.user} is connected!")


# Load cogs
@client.command()
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')


# Unload cogs
@client.command()
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')


# Load cogs
async def load_cogs():
    # Get the base path, then iterate through the cog folder
    path = os.path.dirname(os.path.abspath(__file__))
    for filename in os.listdir(os.path.join(path, 'cogs')):
        # Load in python files in the cogs folder
        if filename.endswith('.py'):
            await load(None, filename[:-3])
            # client.load_extension(f'cogs.{filename[:-3]}')

# Start the bot
client.run(token)

import os
import discord
from discord.ext import commands


token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=['<@!1026624616552218684> ', '<@1026624616552218684> '], intents=intents)


@client.event
async def on_ready():
    await load_cogs()
    print(f"{client.user} is connected!")


# Load cogs
@client.command()
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')


# Load cogs
async def load_cogs():
    path = os.path.dirname(os.path.abspath(__file__))
    for filename in os.listdir(os.path.join(path, 'cogs')):
        if filename.endswith('.py'):
            await load(None, filename[:-3])
            # client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)

import os
import requests
import random
import discord
from discord.ext import commands

import tools

token = os.getenv("DISCORD_TOKEN")
deeptoken = os.getenv("DEEPAI_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=['<@!1026624616552218684> ', '<@1026624616552218684> '], intents=intents)

messages_since_post = 50.0
min_messages_for_post = 10.0
max_messages_for_post = 100.0
max_post_prob = 0.5


# Once the bot is ready, load cogs (commands)
# and print a message to verify connection
@client.event
async def on_ready():
    await load_cogs()
    print(f"{client.user} is connected!")


# Check messages to randomly turn text to images if valid
@client.event
async def on_message(message):
    txt = message.content
    channel = message.channel
    author = message.author
    if str(author) != 'CaptainCaption#6344' and txt is not None and txt != '' and not '1026624616552218684' in txt:
        global messages_since_post
        probability = min(max_post_prob * (messages_since_post - min_messages_for_post) / (max_messages_for_post - min_messages_for_post), max_post_prob)
        if probability > random.random():
            # Run deepai text2image
            req = requests.post("https://api.deepai.org/api/text2img",
                                data={'text': txt},
                                headers={'api-key': deeptoken})

            imlink = req.json()['output_url']
            await tools.post_img(channel, imlink)
            messages_since_post = 0.0
        else:
            messages_since_post += 1.0
    await client.process_commands(message)


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

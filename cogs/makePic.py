import os
import requests
import discord
from discord.ext import commands

import tools

deeptoken = os.getenv("DEEPAI_TOKEN")


class MakePic(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def makepic(self, context, *, message=None):
        if message is None:
            imlink = requests.get('https://source.unsplash.com/random/1200x800', allow_redirects=False).headers['Location']
        else:
            req = requests.post("https://api.deepai.org/api/text2img",
                                 data={'text' : message},
                                 headers={'api-key' : deeptoken})

            imlink = req.json()['output_url']
        await tools.post_img(context, imlink)


async def setup(client):
    await client.add_cog(MakePic(client))
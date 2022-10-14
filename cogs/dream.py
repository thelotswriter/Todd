import os
import requests
import discord
from discord.ext import commands

import tools

deeptoken = os.getenv("DEEPAI_TOKEN")

attachment_error_text = 'Please be sure to attach an image.'


# Cog for applying a "dream" filter
class Dream(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dream(self, context, *, message=None):
        # If there is an image, get the image url and use the deepdream api function
        if tools.image_attached(context.message):
            attachment = context.message.attachments[0]
            imgurl = attachment.url
            req = requests.post("https://api.deepai.org/api/deepdream",
                                data={'image': imgurl},
                                headers={'api-key': deeptoken})

            imlink = req.json()['output_url']
            await tools.post_img(context, imlink)
        else:
            await context.send(attachment_error_text)


async def setup(client):
    await client.add_cog(Dream(client))

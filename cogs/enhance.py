import os
import requests
import discord
from discord.ext import commands

import tools

deeptoken = os.getenv("DEEPAI_TOKEN")

attachment_error_text = 'Please be sure to attach an image.'


class Enhance(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def enhance(self, context, *, message=None):
        if tools.image_attached(context.message):
            attachment = context.message.attachments[0]
            imgurl = attachment.url
            req = requests.post("https://api.deepai.org/api/torch-srgan",
                                data={'image': imgurl},
                                headers={'api-key': deeptoken})

            imlink = req.json()['output_url']
            await tools.post_img(context, imlink)
        else:
            await context.send(attachment_error_text)


async def setup(client):
    await client.add_cog(Enhance(client))

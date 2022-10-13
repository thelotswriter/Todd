import discord
import requests
import os

whiteList = ['bmp','jpeg','jpg','png']


def image_attached(message):
    if message is not None:
        if message.attachments:
            attachment = message.attachments[0]
            if attachment.filename.split('.')[-1] in whiteList:
                return True
    return False

async def post_img(context, imlink):
    imdata = requests.get(imlink).content
    with open('temp.jpg', 'wb') as handler:
        handler.write(imdata)
    await context.send(file=discord.File('temp.jpg'))
    os.remove('temp.jpg')

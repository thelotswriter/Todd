import discord
import requests
import os

# Tools used in the bot's commands

# List of acceptable image types to process
whiteList = ['bmp','jpeg','jpg','png']


# Check if an image is attached to the message
def image_attached(message):
    if message is not None:
        # Return 0 if no attachments, otherwise this will be true
        if message.attachments:
            attachment = message.attachments[0]
            # If the extension is whitelisted, this is an image
            if attachment.filename.split('.')[-1] in whiteList:
                return True
    return False


# Post an image to the given context, converting from a separate URL to an image
async def post_img(context, imlink):
    imdata = requests.get(imlink).content
    with open('temp.jpg', 'wb') as handler:
        handler.write(imdata)
    await context.send(file=discord.File('temp.jpg'))
    # After sending the image to discord it is no longer needed
    os.remove('temp.jpg')

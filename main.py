import os
import io
import discord
from discord.ext import commands
import json
import requests
import PIL
from PIL import Image

# discord bot
bot = commands.Bot(command_prefix="!")

# Opening JSON file with pfps
data = open('sample.json', )

# Location of completed merged images
save_img_folder = 'dressed_pfps/'

# Location to store pfps downloaded from image urls in JSON file
pfp_folder = 'clean_pfps/'

# Returns JSON object as a dictionary
pfp_atts = json.load(data)

# Search for the pfp id in the JSON dictionary and return the image URL associated with that id. You'll need to update the keys to match what's in your JSON delattr

# Need to add error handling

def get_pfp_img_url(id):
    for pfp in pfp_atts:
        if id == pfp['smbId']:
            return pfp['imageSrc']


# Downloads the pfp from the image URL and saves it in a directory

def download_image(url, image_file_path):
    r = requests.get(url, timeout=4.0)
    if r.status_code != requests.codes.ok:
        assert False, 'Status code error: {}.'.format(r.status_code)

    with Image.open(io.BytesIO(r.content)) as im:
        im.save(image_file_path)


# Combines the pfp image with a transparent png of the attribute  and saves it to an output directory


def get_dressed(pfp_id):
    url = (get_pfp_img_url(pfp_id))

    download_image(url, pfp_folder + str(pfp_id) + '.png')

# This combines the images 

    pfp = Image.open(pfp_folder + str(pfp_id) + '.png')
    outfit = Image.open("outfit.png")

    pfp.paste(outfit, (0, 0), mask=outfit)
    pfp.save(save_img_folder + 'dressed' + str(pfp_id) + '.png')

    return


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


# !newfit command executes the get_dressed function and returns the resulting image. It accepts a value between 1 and 5000. Update this to use the command name you want and the values to fit the range of your project


@bot.command(name="newfit")
async def newfit(ctx, arg: int):
    try:
        if 0 <= arg <= 5001:
            get_dressed(str(arg))
            await ctx.channel.send(file=discord.File(save_img_folder + 'dressed' + str(arg) +'.png'))
    except:
        await ctx.send('Please enter a valid number between 1 and 5000')

bot.run(os.getenv('TOKEN'))

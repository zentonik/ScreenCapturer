import discord
from discord.ext import commands
from PIL import ImageGrab
import time
import os

TOKEN = 'Token' # token here
CHANNEL_ID = 1281311409992634397 # channel

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def capture_screenshot():
    filename = f"screenshot_{int(time.time())}.png"
    screenshot = ImageGrab.grab()
    screenshot.save(filename)
    return filename

@bot.event
async def on_ready():
    pass

@bot.command()
async def capture(ctx):
    if ctx.channel.id != CHANNEL_ID:
        return

    filename = capture_screenshot()
    
    channel = bot.get_channel(CHANNEL_ID)
    with open(filename, 'rb') as f:
        await channel.send(file=discord.File(f))

    os.remove(filename)
    await ctx.send("Screenshot captured and sent.")

bot.run(TOKEN)

# type !capture inside the channel to get the pic
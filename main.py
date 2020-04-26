import discord
from discord.ext import commands
from random import randint
from dotenv import load_dotenv
import os

# .ENV usage.json
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Set bot prefix
client = commands.Bot(command_prefix='+')

# Custom Help Command
@client.command()
async def info(message):

    embed = discord.Embed(
        color=randint(0, 0xffffff)
    )
    embed.set_author(name='Here is the list of available commands:')
    await message.channel.send(embed=embed)

# Cogs extention loading
for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[: -3]}')

# Token Setup
client.run(BOT_TOKEN)
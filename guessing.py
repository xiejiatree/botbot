import discord
from discord.ext import commands
from discord import Embed
import datetime
import logging
import os

logging.basicConfig(level=logging.INFO)
print(os.getcwd())
#Initialize bots
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "!", intents = intents, shard_count = 1)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    #bot.load_extension('cogs.GoToSleep')
    await bot.load_extension('cogs.minimal')
    try:
        await bot.load_extension('cogs.haiku_count')
        print('Haiku cog loaded successfully!')
    except Exception as e:
        print(f'Failed to load example cog: {e}')
    print(f'Loaded Extensions: {bot.cogs}')

    # practice a tell me about yourself elevator pitch, review this with the speaking fellows, about two minutes
    # sample projects: what you did, what you knwo about it 
    #Just hit the hot points and keep going. If this guy is trying to hire an intern, he wants to see CODE. 

bot.run('MTI4MzY2MDM0NzY1NTMyMzczMA.GbKN-a.08FhL96pKgCQPLnnhJkrG4pFCDtToWvRP4fzX8')
    #Token = MTI4MzY2MDM0NzY1NTMyMzczMA.GORXuQ.AEBreRf596UGpLtRH_b9oWiJy0IjC8FJnz-4pA
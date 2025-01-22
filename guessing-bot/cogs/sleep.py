from discord.ext import commands
import datetime

class Sleep(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sleep = {}
    
    @client.event
    async def on_message(message):  # this event is called when a message is sent by anyone
        await ctx.send('I caught you messaging.')

async def setup(bot):
    await bot.add_cog(Sleep(bot))

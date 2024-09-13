from discord.ext import commands

class SampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', help='Responds with Pong!')
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command(name='say', help='Makes the bot say a message.')
    async def say(self, ctx, *, message: str):
        await ctx.send(message)

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages from the bot itself
        if message.author == self.bot.user:
            return

        # Respond to a specific message
        if 'hello' in message.content.lower():
            await message.channel.send('Hello there!')

    @commands.command(name='add', help='Adds two numbers.')
    async def add(self, ctx, a: int, b: int):
        result = a + b
        await ctx.send(f'The result of {a} + {b} is {result}')

async def setup(bot):
    await bot.add_cog(SampleCog(bot))

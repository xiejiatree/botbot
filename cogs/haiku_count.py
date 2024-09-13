from discord.ext import commands
from discord import Embed
import discord

class HaikuCount(commands.Cog):
    #constructor
    def __init__(self, bot):
         self.bot = bot
         self.haiku_count = {}
    
    @commands.command(name='HaikuCount')
    async def haiku_count_command(self, ctx):
        channel = discord.utils.get(ctx.guild.channels, name='poetry-slam')
        messages = []
        
        if not channel:
            await ctx.send('Channel "poetry-slam" not found.')
            return

        #Scan the past 1000 messages
        async for message in channel.history(limit = 1000):
            #print('scanned messsages')
            if message.embeds and message.author.name=='HaikuBot':
                #print('message.embeds==true')
                for embed in message.embeds:
                    #print('starting to look at embeds')
                    #HaikuBot does not have embed fields.
                    if embed.footer:
                        if '- ' in embed.footer.text:
                            messages.append(embed.footer.text[2:])
        print(messages)
        #sets dictionary counts to null values. 
        self.haiku_count.clear()



        for message in messages:
            user_id = message

            print(user_id)
            if user_id in self.haiku_count:
                self.haiku_count[user_id] += 1
            else:
                self.haiku_count[user_id] = 1
        #logic for people who changed users. 
        self.haiku_count['deadbeat8058']+=self.haiku_count['DB']
        del self.haiku_count['DB']

        #Create an embedded message
        embed = Embed(title="Haiku Count", description="", color=0x00ff00)
        #a common pattern is to sort complex objects using some of the object's indices as keys.... x[1] assigns a sequential number, dependent on haiku_count.items() which are values
        #haiku_count.keys() is there also 
        sorted_haiku_count = sorted(self.haiku_count.items(), key=lambda x: x[1], reverse = True)
        
        for index, (user_id, count) in enumerate(sorted_haiku_count, start=1):
                #Fetch user object to get the username if needed, probably not happening but will find a way
                counter = str(count)
                try:
                    user = await self.bot.fetch_user(int(user_id))
                    username = user.name
                except:
                    username = user_id  #allback to user ID if user cannot be fetched

                embed.add_field(name=f"{index}. {username}:\t{counter}", value = "",inline=False)
            
        print(self.haiku_count)
            
        await ctx.send(embed=embed)

    @commands.command(name='TalkToMe')
    async def talk_to_me(self, ctx):
        await ctx.send('Leave me alone')
    
    @commands.command(name='shutdown')
    async def shutdown(self, ctx):
        if ctx.author.id == 302967707039563777:  # my user id
            print("Shutting down...")
            await self.bot.close()
        else:
            return
    
async def setup(bot):
    await bot.add_cog(HaikuCount(bot))




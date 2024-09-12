import discord
from discord.ext import commands
from discord import Embed
#Select the python interpreter based on whichever python your discord.py has downloaded to. 3.11


intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)


haiku_count = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='HaikuCount')
async def haiku_count_command(ctx):
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
                if '- ' in embed.footer.text:
                    messages.append(embed.footer.text[2:])
    print(messages)
    #sets dictionary counts to null values. 
    haiku_count.clear()

    for message in messages:
        user_id = message
        print(user_id)
        if user_id in haiku_count:
            haiku_count[user_id] += 1
        else:
            haiku_count[user_id] = 1

    #Create an embedded message
    embed = Embed(title="Haiku Count", description="", color=0x00ff00)
    #a common pattern is to sort complex objects using some of the object's indices as keys.... x[1] assigns a sequential number, dependent on haiku_count.items() which are values
    #haiku_count.keys() is there also 
    sorted_haiku_count = sorted(haiku_count.items(), key=lambda x: x[1], reverse = True)
    
    for index, (user_id, count) in enumerate(sorted_haiku_count, start=1):
            #Fetch user object to get the username if needed, probably not happening but will find a way
            counter = str(count)
            try:
                user = await bot.fetch_user(int(user_id))
                username = user.name
            except:
                username = user_id  #allback to user ID if user cannot be fetched

            embed.add_field(name=f"{index}. {username}:\t{counter}", value = "",inline=False)
        
    print(haiku_count)
        
    await ctx.send(embed=embed)


bot.run('MTI4MzY2MDM0NzY1NTMyMzczMA.GORXuQ.AEBreRf596UGpLtRH_b9oWiJy0IjC8FJnz-4pA')
#Token = MTI4MzY2MDM0NzY1NTMyMzczMA.GORXuQ.AEBreRf596UGpLtRH_b9oWiJy0IjC8FJnz-4pA

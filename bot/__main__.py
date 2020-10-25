import discord                                                                  #  Import discord library
from discord.ext import commands                                                #  From discord library import commands
import config
import token

bot = discor.Client()
bot = commands.Bot(command_prefix=config.PREFIX)                                #  Import bot prefix from config file

@bot.event
async def on_ready():
    print('Logged in as')                                                       #  If bot is ready print this message in console
    print(bot.user.name)                                                        #  Print in console bot name
    print(bot.user.id)                                                          #  Print in console bot id

@bot.event
async def on_message(message):
    if message.author == bot.user:                                              #  If user is bot
        return                                                                  #  do nothing

    await bot.process_command(message)                                          #  Process commands

@bot.command()
async def timer(ctx):
    count = 320                                                                 #  Time in seconds
    countdown = await ctx.message.channel.send('**{}**'.format(count))          #  Send first message to discord channel
    for i in range(count, -1, -1):
        await asyncio.sleep(1)                                                  #  Wait 1 second
        await countdown.edit(content='**{}**'.format(i))                        #  Change message content
        if i == 0:
            await countdown.edit(content='**Time out**')                        #  Change message content


bot.run(token.TOKEN)                                                           #  Run bot

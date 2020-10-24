import discord
from discord.ext import commands


bot = discor.Client()
bot = commands.Bot(command_prefix=config.PREFIX)

@bot.event
async def on_message(message):
    if message.author == bot.user:                                              #  If user is bot do nothing
        return
    await bot.process_command(message)                                          #  Process commands

@bot.command()
async def timer(ctx):
    count = 320  # Time in seconds
    countdown = await ctx.message.channel.send('**{}**'.format(count))          #  Send first message to discord channel
    for i in range(count, -1, -1):                                              #  For loop
        await asyncio.sleep(1)                                                  #  Wait 1 second
        await countdown.edit(content='**{}**'.format(i))                        #  Change message content
        if i == 0:                                                              #  If i = 0 someting
            await countdown.edit(content='**Time out**')                        #  Change message content


bot.run(config.TOKEN)

import discord
bot = discor.Client()
bot = commands.Bot(command_prefix=config.PREFIX)

bot.run(config.TOKEN)

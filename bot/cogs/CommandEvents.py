from discord.ext import commands

class CommandEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_command_completion(self, ctx):
        print('{} was invoked successfully.'.format(ctx.command.name))

def setup(bot):
    bot.add_cog(CommandEvents(bot))

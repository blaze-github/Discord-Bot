"""

BSD 3-Clause License

Copyright (c) 2020, blaze-github
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
import discord
from discord.ext import commands
import os
import config

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    global help_commands_list

    help_commands_list = {'Bot'   :    '?bot help',
                          'Vote'   :   '?help vote',
                          'Attack' :   '?help attack'}

    @commands.group(name = 'help', invoke_without_command = True)
    async def HelpCommand(self, ctx):
        file = 'banners/out.png'

        main_help_command_embed = discord.Embed(color=discord.Color(0xe74c3c))

        main_help_command_embed.set_author(name='{} | Help'.format(self.bot.user.name), url = '', icon_url=self.bot.user.avatar_url)
        # main_help_command_embed.set_thumbnail(url=ctx.guild.icon_url)

        # main_help_command_embed.title = '**Bot help**'
        # main_help_command_embed.description = 'Bot help description'

        for command, description in help_commands_list.items():
            main_help_command_embed.add_field(name = '**{}**'.format(command), value = '`{}`'.format(description), inline = True)

        default_server_banner_url = discord.File('banners/{}.png'.format(config.SERVER_NAME), filename = '{}.png'.format(config.SERVER_NAME))

        main_help_command_embed.set_image(url = 'attachment://{}.png'.format(config.SERVER_NAME))
        main_help_command_embed.set_footer(icon_url=ctx.message.author.avatar_url ,text=' This message was invoked successfully by {}'.format(ctx.message.author))

        await ctx.channel.send(file = default_server_banner_url, embed = main_help_command_embed)

    @HelpCommand.command(name = 'vote')
    async def vote_help_subcommand(self,ctx):
        await ctx.channel.send('This is vote help command')



def setup(bot):
    bot.add_cog(HelpCommands(bot))

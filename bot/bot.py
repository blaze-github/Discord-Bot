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

import discord                                                                  #  Import discord library
from discord.ext import commands                                                #  From discord library import commands
import config
import token

bot = discord.Client()
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

bot.load_extension('cogs.CommandEvents')
bot.run(config.TOKEN)                                                           #  Run bot

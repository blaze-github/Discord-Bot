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
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import config

class BotBanners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # banner_map = [[1] * 12 for n in range(3)]
        #
        #
        banner_width = 600
        banner_height = 150
        icon_width = 50
        icon_height = 50
        #
        # x_pos, y_pos = 0, 0
        #
        # banner = Image.new('RGB', (banner_width, banner_height), (0,0,0))
        # text_str = config.SERVER_NAME
        # # url = 'https://sun9-21.userapi.com/HrNx-ZHuLZG36DUuegsvX6XyTfD-4HfbPsoihw/TlGdyw2vQ4o.jpg'
        # # response = requests.get(url)
        # # icon = Image.open(BytesIO(response.content))
        # icon = Image.open('banners/default.png')
        # result = Image.new('RGB', (banner_width, banner_height), (0,0,0))
        #
        # result.paste(banner, (0,0))
        #
        # for row in banner_map:
        #     for col in row:
        #         result.paste(icon,(x_pos,y_pos))
        #         x_pos = x_pos + icon_width
        #     y_pos = y_pos + icon_height
        #     x_pos = 0
        #
        # result.save('banners/{}.png'.format(text_str))



        banner = Image.open('banners/default1.png')
        # server_logo = selfbot.guild.icon_url
        # banner.paste(server_logo)


        canvas = ImageDraw.Draw(banner)
        text_str = config.SERVER_NAME
        font = ImageFont.truetype('font/Lato-Bold.ttf', size=48)
        text_width, text_height = canvas.textsize(text_str, font=font)

        text_x_pos = int((banner_width - text_width) / 2)
        text_y_pos = int((banner_height - text_height) / 2)

        canvas.text((text_x_pos + 5,text_y_pos + 5),text_str, font = font, fill=(0, 0, 0))
        canvas.text((text_x_pos,text_y_pos),text_str, font = font, fill=(225, 255, 255))

        banner.save('banners/{}.png'.format(text_str))


    @commands.command()
    async def DAEB(slef, ctx):
        await ctx.channel.send(file = discord.File('default_server_banner.png'))


def setup(bot):
    bot.add_cog(BotBanners(bot))

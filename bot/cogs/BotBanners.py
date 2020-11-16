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
import random
import multiprocessing
import autopep8


class BotBanners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        BotBanners.generate_main_banner(self)

    @commands.Cog.listener()
    async def on_ready(self):
        with open('users.txt', 'w') as f:
            for guild in self.bot.guilds:
                async for member in guild.fetch_members(limit=None):
                    print(member.avatar_url, file=f)

    def generate_main_banner(self):
        url = []
        with open('users.txt', 'r') as f:
            for line in f:
                url.append(line)
                print(random.choice(url))

        banner_map = [[1] * 12 for n in range(4)]

        banner_width = 600
        banner_height = 150
        icon_width = 50
        icon_height = 50

        x_pos, y_pos = 0, 0

        banner = Image.new('RGB', (banner_width, banner_height), (0, 0, 0))
        text_str = config.SERVER_NAME
        # icon = Image.open('banners/default.png')
        result = Image.new('RGB', (banner_width, banner_height), (0, 0, 0))
        result.paste(banner, (0, 0))
        for row in banner_map:
            for col in row:
                for image in row:
                    image = 'https://play-lh.googleusercontent.com/b0p_qGMKAcQoT0YWHzhTsol0j1rD6AMdgfvMKUFmR8IDXnYfNeldH7dfO4BoUqID2k0'
                    icon = Image.open(BytesIO(requests.get(image).content))
                    icon = icon.resize((icon_width, icon_height), Image.ANTIALIAS)
                result.paste(icon, (x_pos, y_pos))
                x_pos = x_pos + icon_width
            y_pos = y_pos + icon_height
            x_pos = 0

        canvas = ImageDraw.Draw(result)
        font = ImageFont.truetype('font/Lato-Bold.ttf', size=48)
        text_width, text_height = canvas.textsize(text_str, font=font)

        text_x_pos = int((banner_width - text_width) / 2)
        text_y_pos = int((banner_height - text_height) / 2)

        canvas.text((text_x_pos + 5, text_y_pos + 5), text_str, font=font, fill=(0, 0, 0))
        canvas.text((text_x_pos, text_y_pos), text_str, font=font, fill=(225, 255, 255))

        result.save('banners/{}.png'.format(text_str))

def setup(bot):
    bot.add_cog(BotBanners(bot))



# TO DO:

# - Fix bug
#     cogs.BotBanners' raised an error:
#     UnidentifiedImageError:
#     cannot identify image file <_io.BytesIO object at 0x7f57d497c540>

#  - Migrate configs
#     Migrate configs from config.py to dotenv (.env)

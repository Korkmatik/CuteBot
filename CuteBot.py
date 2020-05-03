# MIT License
#
# Copyright (c) 2020 Korkmatik
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import discord
import logging

from helpers import read_secrets, get_random_compliment, get_random_itachi_quote

# Channel ID of the Text Channel dedicated to the Cute Bot
from mySpecials import get_cute_bot_channel_id
# Dictionary with channels which can be used by Cute Bot (key=Channel Name, value=Channel ID)
from mySpecials import get_channels
# Returns cute bot's text channel name
from mySpecials import get_cute_bot_channel_name
# Returns a dictionary with the hangman text channel name and ID
from mySpecials import get_hangman_channel, get_hangman_channel_name

from Games.Hangman import Hangman


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class CuteBot(discord.Client):

    CUTE_BOT_CHANNEL_ID = get_cute_bot_channel_id()
    CUTE_BOT_CHANNEL_NAME = get_cute_bot_channel_name()
    HANGMAN_CHANNEL = get_hangman_channel()
    HANGMAN_CHANNEL_NAME = get_hangman_channel_name()
    CHANNELS = get_channels()

    async def on_ready(self):
        logging.debug("Connected")

    async def on_message(self, message):
        message.content = discord.utils.escape_mentions(message.content)
        message.content = discord.utils.escape_markdown(message.content)

        if message.author == self.user:
            return

        if "krass" in message.content.lower():
            await message.channel.send("Danke du auch!")

        # Checking if the command syntax is used
        if not message.content.startswith("!"):
            logging.debug("Doesn't start with '!'")
            return

        if str(message.channel) == self.CUTE_BOT_CHANNEL_NAME:
            # Commands for CuteBot's channel
            if message.content == "!hello":
                await message.channel.send(f"Hello {message.author.mention}")
            elif message.content == "!whoami":
                await message.author.send("You are my senpai :heart:")
            elif message.content == "!stats":
                async with message.channel.typing():
                    current_user = message.author
                    count_messages = 0
                    count_bot_interaction = 0

                    for channel in self.CHANNELS.keys():
                        channel_id = self.CHANNELS[channel]
                        ch = self.get_channel(channel_id)
                        messages = await ch.history(limit=400).flatten()

                        for m in messages:
                            if m.author.id == current_user.id:
                                count_messages += 1
                                if channel_id == self.CUTE_BOT_CHANNEL_ID:
                                    count_bot_interaction += 1

                    embed = discord.Embed(title=f"{current_user.name}'s stats", description="")
                    embed.add_field(name="Number messages you send", value=f"{count_messages}")
                    embed.add_field(name="Number of interactions you had with me", value=f"{count_bot_interaction}")
                    await message.channel.send(content=None, embed=embed)
            elif message.content == "!cute":
                role = discord.utils.get(message.guild.roles, name='Cute')
                try:
                    await message.author.add_roles(role)
                except:
                    await message.channel.send("Sorry, the force isn't with me. I was not able to make you cute ... (っ °Д °;)っ")
            elif message.content == "!makemehappy":
                await message.channel.send(get_random_compliment())
            elif message.content == "!itachi":
                await message.channel.send(get_random_itachi_quote())
            elif message.content == "!help":
                embed = discord.Embed(title=f"Help", description="Commands which I understand")
                embed.add_field(name="!hello", value="I will greet you!")
                embed.add_field(name="!whoami", value="I will send you a private message ヾ(•ω•`)o")
                embed.add_field(name="!stats", value="I will show your stats!")
                embed.add_field(name="!cute", value="I will make you cute!")
                embed.add_field(name="!makemehappy", value="I will make you happy!")
                embed.add_field(name="!itachi", value="Just use it if you want to read a great quote!")
                await message.channel.send(content=None, embed=embed)
        elif str(message.channel) == self.HANGMAN_CHANNEL_NAME:
            # Hangman game
            await message.channel.send(Hangman.get_message(message.content))

    async def on_member_join(self, member):
        channel = self.get_channel(self.CUTE_BOT_CHANNEL_NAME)
        await channel.send(f"Oh look! A new member! Welcome {member.mention}! o(*°▽°*)o")


if __name__ == '__main__':
    token, serverID = read_secrets()

    b = CuteBot()
    b.run(token)

import discord
import logging

from helpers import read_secrets, get_random_compliment

# Channel ID of the Text Channel dedicated to the Cute Bot
from mySpecials import get_cute_bot_channel_id
# Dictionary with channels which can be used by Cute Bot (key=Channel Name, value=Channel ID)
from mySpecials import get_channels
# Returns cute bot's text channel name
from mySpecials import get_cute_bot_channel_name


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class CuteBot(discord.Client):

    CUTE_BOT_CHANNEL_ID = get_cute_bot_channel_id()
    CUTE_BOT_CHANNEL_NAME = get_cute_bot_channel_name()
    CHANNELS = get_channels()

    async def on_ready(self):
        logging.debug("Connected")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if "krass" in message.content.lower():
            await message.channel.send("Danke du auch!")

        # Checking if the command syntax is used
        if not message.content.startswith("!"):
            logging.debug("Doesn't start with '!'")
            return

        # Checking if message was send in cute bot's channel
        logging.debug(f"Channel: {message.channel}")
        if str(message.channel) != self.CUTE_BOT_CHANNEL_NAME:
            logging.debug("Not cute bot's home")
            return

        # Commands
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
        elif message.content == "!help":
            embed = discord.Embed(title=f"Help", description="Commands which I understand")
            embed.add_field(name="!hello", value="I will greet you!")
            embed.add_field(name="!whoami", value="I will send you a private message ヾ(•ω•`)o")
            embed.add_field(name="!stats", value="I will show your stats!")
            embed.add_field(name="!cute", value="I will make you cute!")
            embed.add_field(name="!makemehappy", value="I will make you happy!")
            await message.channel.send(content=None, embed=embed)

    async def on_member_join(self, member):
        channel = self.get_channel(self.CUTE_BOT_CHANNEL_NAME)
        await channel.send(f"Oh look! A new member! Welcome {member.mention}! o(*°▽°*)o")


if __name__ == '__main__':
    token, serverID = read_secrets()

    b = CuteBot()
    b.run(token)

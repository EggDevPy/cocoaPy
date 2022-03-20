import asyncio
import time

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands

from utils.config import token, BOTENV_ID

Intents = discord.Intents.all()
client = discord.Client(intents=Intents)
tree = app_commands.CommandTree(client)

'''
3.20.2022 | 4:41pm | Charlotte #4 -
~~~~~~~~

- Commands Registered, I have added a loading.py file.
Info for that included in #4 commit, as well as file comments.

- Added activity presence on ln 53

'''


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.owner_id = 384459643545583627
        self.init_ext = [
            'cogs.testing',
            'cogs.loading'
        ]

    async def on_ready(self):
        print('^^ Extensions/App Commands ^^\n')
        print(time.strftime("Sync'd all application commands\n@ %H:%M:%S\n"
                            f"%m/%d/%Y\n"
                            f"-----"))
        print(f'Logged in as {self.user}')
        print('-----')
        await self.tree.sync(guild=discord.Object(886621065554575410))
        await self.change_presence(status=discord.Status.online,
                                   activity=discord.Game('with code'))

    async def setup_hook(self):
        self.session = aiohttp.ClientSession()
        for ext in self.init_ext:
            await self.load_extension(ext)
            print(ext)


async def main():
    bot = MyBot(
        command_prefix=";;",
        intents=discord.Intents(
            presences=True,
            members=True,
            messages=True,
            guilds=True,
            message_content=True),
    )

    async with bot:
        await bot.start(token,
                        reconnect=True)


async def on_member_join(member):
    """Im not even sure this would work"""
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)


if __name__ == '__main__':
    asyncio.run(main())

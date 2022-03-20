import discord
from discord import app_commands
from discord.ext import commands, tasks

from utils.config import token

intents = discord.Intents.all()
intents.message_content = True
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

'''
3.20.2022 | 12:54am | Charlotte -
The bot runs, but is unresponsive. Nothing prints to the console, 
and it appears I've not linked application commands.

Documentation available:
https://discordpy.readthedocs.io/en/latest/index.html#getting-started

https://gist.github.com/Rapptz/c4324f17a80c94776832430007ad40e6

https://github.com/Rapptz/discord.py/tree/master/examples

https://discordpy.readthedocs.io/en/master/migrating.html#python-version-change

and the discord.py server.

'''


class MyClient(discord.Client):
    async def on_ready(self):
        """None of these events work, seemingly."""
        print(f"Sync'd all application commands @%H:%M:%S\n"
              f"%m/%d/%Y\n"
              f"-----")
        print(f'Logged in as {client.user}')
        print('-----')
        await tree.sync()



    async def on_member_join(self, member):
        """Im not even sure this would work"""
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)


client.run(token,
           reconnect=True)

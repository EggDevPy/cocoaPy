import time

import discord
from discord import app_commands


from utils.config import token

intents = discord.Intents.all()
intents.message_content = True
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

'''
3.20.2022 | 11:33am | Charlotte -
The bot runs, and now prints to the console.
No commands seem to have registered.

Documentation available:
https://discordpy.readthedocs.io/en/latest/index.html#getting-started

https://gist.github.com/Rapptz/c4324f17a80c94776832430007ad40e6

https://github.com/Rapptz/discord.py/tree/master/examples

https://discordpy.readthedocs.io/en/master/migrating.html#python-version-change

and the discord.py server.

'''
BOTENV_ID = 886621065554575410


@client.event
async def on_ready():
    await client.wait_until_ready()
    await tree.sync()

    print(time.strftime("Sync'd all application commands  @%H:%M:%S\n"
                        f"%m/%d/%Y\n"
                        f"-----"))
    print(f'Logged in as {client.user}')
    print('-----')


async def setup_hook() -> None:
    await tree.sync()


async def on_member_join(member):
    """Im not even sure this would work"""
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)


client.run(token,
           reconnect=True)

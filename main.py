import asyncio
import time

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands

from utils.config import token

import PySimpleGUI as sg
import platform, \
    socket, \
    re, \
    uuid, \
    json, \
    psutil, \
    logging

Intents = discord.Intents.all()
client = discord.Client(intents=Intents)
tree = app_commands.CommandTree(client)

'''
3.22.2022 | 6:52pm | Charlotte -
~~~~~~~~

- Invite command removed in favor of bigger, better about command

- Working with buttons, links

'''


def get_prefix(bot, message):
    prefixes = [';;']
    if not message.guild:
        return ['?']
    return commands.when_mentioned_or(*prefixes)(bot, message)


def getSystemInfo():
    try:
        info = {}
        info['platform'] = platform.system()
        info['platform-release'] = platform.release()
        info['platform-version'] = platform.version()
        info['architecture'] = platform.machine()
        info['hostname'] = socket.gethostname()
        info['processor'] = platform.processor()
        info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


json.loads(getSystemInfo())


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.owner_id = 384459643545583627
        self.init_ext = [
            'cogs.loading',
            'cogs.misc',
            'cogs.server'
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

        sg.theme('LightGreen3')

        e = json.loads(getSystemInfo())

        layout = [
            [sg.Text(f"Logged in as {self.user}")],
            [sg.Text(f"Bot ID: {self.user.id}")],
            [sg.Text(f"# of Guilds in: {len(self.guilds)}")],
            [sg.Text("Initial Extensions:")],
            [sg.Listbox(values=(self.init_ext), size=(30, 3))],
            [sg.Text("Current issues: \n"
                     "https://github.com/EggDevPy/cocoaPy/issues")],
            [sg.Text("System Info:\n")],
            [sg.Multiline(f"{e}", size=(40,40))],

        ]
        window = sg.Window('CocoaPy', layout, resizable=True, size=(300, 400))
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            print("GUI Exited")
        window.close()

    async def setup_hook(self):
        self.session = aiohttp.ClientSession()
        for ext in self.init_ext:
            await self.load_extension(ext)
            print(ext)

    async def on_member_join(self, member):
        """This works on channels that are set to system messages - hence guild.system_channel"""
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome to {guild.name}, {member.mention}!'
            await guild.system_channel.send(to_send)


async def main():
    bot = MyBot(
        command_prefix=get_prefix,
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


if __name__ == '__main__':
    asyncio.run(main())



import traceback
from typing import Literal

import discord
from discord import app_commands, Embed, AppInfo, Permissions
from discord.ext import commands
from discord.utils import oauth_url


def format_date(dt):
    if dt is None:
        return 'N/A'
    return f'{dt:%A %d, %B %Y • %I:%M %p}'



class About(discord.ui.View):
    def __init__(self):
        super(About, self).__init__(timeout=None)
        self.value = None

        url = 'https://github.com/EggDevPy/cocoaPy'
        serverUrl = 'https://discord.gg/btBCpwQwsK'

        # UI Buttons for the About command, doesn't appear I can actually color the links.
        self.add_item(discord.ui.Button(label='GitHub',
                                        url=url,
                                        style=discord.ButtonStyle.green))
        self.add_item(discord.ui.Button(label='Help Server',
                                        url=serverUrl,
                                        style=discord.ButtonStyle.blurple))


class Feedback(discord.ui.Modal, title='Feeback'):
    """Text inputs declare fields for text input"""
    """https://discordpy.readthedocs.io/en/master/interactions/api.html#modal"""

    name = discord.ui.TextInput(
        label='Username',
        placeholder="Discord username here",

    )
    mail = discord.ui.TextInput(
        label='Email',
        placeholder="Enter your email here",
        required=False
    )
    feedback = discord.ui.TextInput(
        label="Feeback / Suggestions on Cocoa?",
        style=discord.TextStyle.long,
        placeholder='Type message here',
        required=False,
        max_length=300,
    )

    async def on_submit(self, interaction: discord.Interaction):
        """submission button"""
        channel = interaction.guild.get_channel(955127273692995584)  # I coded it so that it will send to a channel
        await interaction.response.send_message(f'Thanks for your feedback, {self.name.value}!',
                                                ephemeral=True)  # Invisible TY message

        await channel.send(content=f"{interaction.user.mention}\n"
                                   f"{self.name.value}\n"
                                   f"{self.mail.value}\n"
                                   f"{self.feedback.value}"
                           )
        """
        These are the stored values from the feedback modal,
        being returned to a channel. We can definitely modify
        this to store values to a database with ease.
        """

    async def on_error(self, error: Exception, interaction: discord.Interaction) -> None:
        """Simple error catch with traceback"""
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

        traceback.print_tb(error.__traceback__)


class Miscellaneous(commands.Cog, app_commands.Group, name="server"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()  # this is now required in this context.

    @app_commands.command()
    async def status(self, interaction: discord.Interaction,
                     status: Literal['online',
                                     'idle',
                                     'dnd'],
                     activity: str):
        before = self.bot.status
        modified = ''.join(activity)
        if before != modified:
            await self.bot.change_presence(status=discord.Status(status),
                                           activity=discord.Game(f"{modified}"))
            await interaction.response.send_message(f"Status changed to {activity} ", ephemeral=True)

    @app_commands.command()
    async def feedback(self, interaction: discord.Interaction):
        """This is where the class object is actually called as a command."""
        await interaction.response.send_modal(Feedback())

    @app_commands.command()
    async def about(self, interaction: discord.Interaction):
        """I replaced the Invite app_command with this, it offers additional info as well as UI views"""
        app_info: AppInfo = await self.bot.application_info()
        permissions = Permissions()
        permissions.update(
            send_messages=True,
            embed_links=True,
            add_reactions=True,
            manage_channels=True,
            manage_webhooks=True,
            manage_roles=True
        )

        em = Embed(title=f"About this bot...",

                   ).set_author(
            name=f"Click here to invite {self.bot.user.name}!",
            icon_url=self.bot.user.avatar.url,
            url=f'{oauth_url(app_info.id, permissions=permissions)}'
        ).set_footer(
            text="Authors: Max & Charlotte"
        )
        em.add_field(name=f"{self.bot.user.name} was created",
                     value=format_date(self.bot.user.created_at), inline=False)
        em.add_field(name=f"{self.bot.user.name} watches over",
                     value=f"{len(self.bot.guilds)} servers, and {len(self.bot.users)} members")
        em.color = discord.Color.random()
        await interaction.response.send_message(embed=em, view=About())


async def setup(bot: commands.Bot) -> None:
    # await bot.add_cog(MyCog(bot))
    # or if you want guild/guilds only...
    await bot.add_cog(Miscellaneous(bot), guilds=[discord.Object(id=886621065554575410)])

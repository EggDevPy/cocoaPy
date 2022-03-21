from typing import List, Literal

import discord
from discord import app_commands, Embed, AppInfo, Permissions
from discord.app_commands import Choice
from discord.ext import commands
from discord.ext.commands import bot_has_permissions, Context
from discord.utils import oauth_url


class Miscellaneous(commands.Cog, app_commands.Group, name="server"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()  # this is now required in this context.

    @app_commands.command(name="invite")
    async def invite(self, interaction: discord.Interaction):
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
        em = Embed(title="Try Cocoa Bot today!",
                   url=f"{oauth_url(app_info.id, permissions=permissions)}"
                   ).set_author(
            name=f"Invite {self.bot.user}",
            icon_url=self.bot.user.avatar.url
        ).set_footer(
            text="Authors: Max & Charlotte"
        )
        em.color = discord.Color.random()
        try:
            await interaction.response.send_message(embed=em)
        except:
            await interaction.response.send_message("Enable embed permissions for me!", ephemeral=True)

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


async def setup(bot: commands.Bot) -> None:
    # await bot.add_cog(MyCog(bot))
    # or if you want guild/guilds only...
    await bot.add_cog(Miscellaneous(bot), guilds=[discord.Object(id=886621065554575410)])

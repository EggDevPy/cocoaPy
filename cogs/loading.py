import discord
from discord import app_commands
from discord.ext import commands

"""
This was supposed to have three functions to assist with bugfixing,
command testing, creation, etc. It doesn't seem they work (as I've implemented them)
as they did with fembot, despite some code rewrite.
~~~~~~~

- Cog load:
Loads cog if previously unloaded (more useful for debugging, or in the case
that you unload a cog.)
~~~~~~~

- Cog unload:
Unloads a cog
~~~~~~~


- Cog reload:
Reloads a cog.
This was the main reason I wanted to write this file,
running this command would allow us to continuously update changes we make,
assuming they're not files outside of the cogs itself, or file changes that the cog is
dependent on.
~~~~~~~

All commands would us dotpath extension. eg: /reload cogs.loading

Charlotte
"""


class Loader(commands.Cog, app_commands.Group, name="cogs"):
    def __init__(self, bot: commands.Bot) -> None:
        """The loading/reloading/etc doesn't seem to work like intended"""
        self.bot = bot
        super().__init__()

    @app_commands.command(name="load-cog")
    @app_commands.guilds(886621065554575410)
    async def cogload(self, interaction: discord.Interaction, cog: str) -> None:
        try:
            await self.bot.load_extension(cog)
        except Exception as e:
            await interaction.response.send_message(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await interaction.response.send_message(f"**`SUCCESS`**")

    @app_commands.command(name="unload-cog")
    async def cogunload(self, interaction: discord.Interaction, cog: str) -> None:
        try:
            await self.bot.unload_extension(cog)
        except Exception as e:
            await interaction.response.send_message(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await interaction.response.send_message(f"**`SUCCESS`**")

    @app_commands.command(name="reload-cog")
    async def cog_reload(self, interaction: discord.Interaction, cog: str):
        try:
            await self.bot.reload_extension(cog)
        except Exception as e:
            await interaction.response.send_message(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await interaction.response.send_message(f"**`SUCCESS`**")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Loader(bot), guilds=[discord.Object(id=886621065554575410)])

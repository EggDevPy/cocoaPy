import discord
from discord.ext import commands
from discord import app_commands


class Test(app_commands.Group):
    def __init__(self, bot):
        self.bot = bot

    group = app_commands.Group(name="Parent",
                               description="...")

    # @app_commands.guild() will define specific guild commands, etc, currently this is a global - which is nice.
    @app_commands.command(name="Top-Command")
    async def top_test(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message('tested', ephemeral=True)

    @group.command(name="sub-command")  # we use the declared group to make a command.
    async def sub_test(self, interaction: discord.Interaction) -> None:
        """ /parent sub-command """
        await interaction.response.send_message("Test subs", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Test(bot))

from typing import List

import discord
from discord import app_commands
from discord.ext import commands


class MyCog(commands.Cog, app_commands.Group, name="testing"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()  # this is now required in this context.

    # @app_commands.guilds(886621065554575410)
    # apparently these names need to be lower case
    @app_commands.command(name="ping")
    async def ping_pong(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"You've been Pinged back!: `{self.bot.latency * 1000:.2f}ms`")

    @app_commands.command()
    async def fruits(self, interaction: discord.Interaction, fruits: str):
        await interaction.response.send_message(f'Your favourite fruit seems to be {fruits}')

    @fruits.autocomplete('fruits')
    async def fruits_autocomplete(self, interaction: discord.Interaction,
                                  current: str,
                                  ) -> List[app_commands.Choice[str]]:
        fruits = ['Banana', 'Pineapple', 'Apple', 'Watermelon', 'Melon', 'Cherry']
        return [
            app_commands.Choice(name=fruit, value=fruit)
            for fruit in fruits if current.lower() in fruit.lower()
        ]


async def setup(bot: commands.Bot) -> None:
    # await bot.add_cog(MyCog(bot))
    # or if you want guild/guilds only...
    await bot.add_cog(MyCog(bot), guilds=[discord.Object(id=886621065554575410)])

from typing import Dict, Iterable

import discord
from discord import app_commands
from discord.ext import commands


"""
None of this works at the moment. Something to do with transformers
I imagine it's an issue with the reactions
"""




def get_emoji_for(thing: int) -> str:
    print(f"Getting emoji {thing}")
    emoji_dict = {
        1: "1️⃣",
        2: "2️⃣",
        3: "3️⃣",
        4: "4️⃣",
        5: "5️⃣",
        6: "6️⃣",
        7: "7️⃣",
        8: "8️⃣",
        9: "9️⃣",
        10: "🔟",
    }
    print(emoji_dict)
    print(f"Got {emoji_dict[thing]}")
    return emoji_dict[thing]


def make_numbered_lists(stuff: Iterable[str]) -> str:
    output = ""
    for index, item in enumerate(stuff, start=1):
        output += f"{get_emoji_for(index)} " + item + "\n\n"
    return output


class server(commands.Cog, app_commands.Group, name="server"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    # @app_commands.command(name='poll')
    # async def poll(self, interaction: discord.Interaction,
    #                question: str,
    #                *choices: str,
    #                **choices_dict: Dict[str, str],
    #
    #                ) -> None:
    #     choices = list(choices)
    #     choices.extend(choices_dict.values())
    #     if not len(set(choices)) != len(choices):
    #         await interaction.response.send_message("Dont dupe", ephemeral=True)
    #         return
    #     try:
    #         PollEmbed = interaction.channel.send_message(
    #             embed=discord.Embed(
    #                 title=f"{question}",
    #                 description=make_numbered_lists(choices),
    #                 color=discord.Color.random()
    #             ).set_author(
    #                 name={f"{interaction.user}"},
    #                 icon_url=str(interaction.user.avatar)
    #             ).set_footer(
    #                 text=f"Time: {interaction.created_at.timestamp()}"
    #             ))
    #     except:
    #         await interaction.response.send_message("Well that fucking sucks. It failed",
    #                                                 ephemeral=True)
    #     else:
    #         await interaction.response.send_message("Cream",
    #                                                 ephemeral=True)
    #         try:
    #             for emoji in map(get_emoji_for, range(1, len(choices) + 1)):
    #                 await PollEmbed.add_reaction(emoji)
    #         except:
    #             await interaction.response.send_message("Well i cant add reactions. Shit",
    #                                                     ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(server(bot),
                      guilds=[discord.Object(id=886621065554575410)])

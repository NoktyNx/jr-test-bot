"""
Return responses data from the 5etools site.

Check them out at https://5etools.com/
"""
import requests
from discord.ext import commands
from helpers import CLASSES, MONSTERS


class DND:
    def __init__(self, bot):
        """
        Init for the DND object.

        Starts requests.gets for json() data types and stores them as
        DND object attributes to manipulate in other methods that the
        Discord bot will use for chat commands

        Theoretical example command:
        Discord User: "!DND.monster.blinkdog"
        Bot response:
            Name: "Blink Dog"
            Type: "Medium Fey"
            Alignment: "Lawful Good"
            Source: "Monster Manual"
            Armor Class: "13"
            etc.
        """
        self.bot = bot
        self.class_json = requests.get(
            "https://5etools.com/data/classes.json?ver=1.53.1")
        self.monster_json = requests.get(
            "https://5etools.com/data/bestiary/bestiary-mm.json?ver=1.53.1")

    async def on_command(self, ctx):
        command = ctx.command.qualified_name
        self.bot.command_stats[command] += 1
        message = ctx.message


@commands.command(hidden=True)
def classes(self, player_class=""):
    """
    Class request information.

    class is a string representing the desired class data.
    info is a string representing the desired class information,
        if specified.
    """
    if player_class:
        class_info['class_name'] = self.class_json.json()[
            'class'][CLASSES[player_class]]['name']  # "Barbarian"
        class_info['source'] = self.class_json.json()['source']  # "PHB"
        #  etc.
    else:

    return class_info

@commands.command(hidden=True)
def monsters(self, monster="", info=""):
    """
    Monster request information.

    monster is a string representing the desired monster data.
    info is a string repreenting the desired monster information,
        if specified.
    """
    return self.monster_json()['monster'][MONSTERS['Aarakocra']['name']

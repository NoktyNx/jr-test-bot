"""
Return responses data from the 5etools site.

Check them out at https://5etools.com/.
"""
import inspect
import requests
from discord.ext import commands
from helpers import CLASSES, MONSTERS


class DND(object):
    def __init__(self, bot):
        """Init for the DND json() objects."""
        self.bot = bot
        self.class_json = requests.get(
            "https://5etools.com/data/classes.json?ver=1.53.1")
        self.monster_json = requests.get(
            "https://5etools.com/data/bestiary/bestiary-mm.json?ver=1.53.1")

        members = inspect.getmembers(self)
        for name, member in members:
            if isinstance(member, commands.Command):
                if member.parent is None:
                    self.add_command(member)


@commands.group()
async def classes(ctx):
    """Displays the list of classes you can choose from."""
    await ctx.send(
        'The following classes have information available:\n'
        'Barbarian, Bard, Cleric\n'
        'To obtain specific information about a class, use '
        '!classes.classname (i.e. to get Barbarian info use '
        '!classes barbarian or !classes Barbarian)')


@classes.command("barbarian".lower())
async def barbarian(ctx):
    """Barbarian class info."""
    await ctx.send(
        "Barbarian class info here. Example output:\n"
        f"Name: {DND.class_json['class'][0]['name']}\n"
        f"Source: {DND.class_json['class'][0]['source']}")

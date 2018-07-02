"""
Return responses data from the 5etools site.

Check them out at https://5etools.com/.
"""
import requests
from discord.ext import commands
from helpers import CLASSES


class DND(object):
    def __init__(self):
        """Init for the DND json() objects."""
        self.monster_json_request = requests.get(
            "https://5etools.com/data/bestiary/bestiary-mm.json?ver=1.53.1")

    def class_info(class_name):
        """Return class info dict for class_name param passed."""
        class_json_request = requests.get(
            f"https://5etools.com/data/class/class-{class_name}.json")
        return class_json_request


@commands.group(case_insensitive=True, pass_context=True)
async def classes(ctx):
    """Displays the list of classes you can choose from."""
    if (len(
        ctx.message.content) <= len('!classes ') and (
            len(ctx.message.content) >= 4)):
        await ctx.send(CLASSES['supported'])


@classes.command(case_insensitive=True,
                 aliases=CLASSES['supported_list'])
async def class_info(ctx):
    """Class info command return for a given class."""
    # Setup
    info = None
    info_dict = {}
    invoked_call = ctx.invoked_with.lower()
    if invoked_call in ctx.command.aliases:
        info = DND.class_info(invoked_call).json()
    else:
        await ctx.send(
            f'Invalid class command: {ctx.message.content}\n'
            f'Please use the !classes command to see supported class options.')
    dice_count = info['class'][CLASSES[invoked_call]]['hd']['number']
    dice_faces = info['class'][CLASSES[invoked_call]]['hd']['faces']
    saving_throws = info['class'][CLASSES[invoked_call]]['proficiency']

    # Build info_dict from Setup.
    info_dict['name'] = info['class'][CLASSES[invoked_call]]['name']
    info_dict['source'] = info['class'][CLASSES[invoked_call]]['source']
    info_dict['hit_dice'] = f"{dice_count}d{dice_faces}"
    info_dict['saving_throws'] = f"{saving_throws[0]}, {saving_throws[1]}"

    # Post built info_dict to chat.
    await ctx.send(
        f"""```md\n[{info_dict['name']}]\n"""
        f"# Source: {info_dict['source']}\n"
        f"# Hit Dice: {info_dict['hit_dice']}\n"
        f"# Proficiencies: 1. Saving Throws: {info_dict['saving_throws']} | "
        f"2. Something: 0\n"
        f"```")

"""
Return responses data from the 5etools site.

Check them out at https://5etools.com/.
"""
import requests
import discord
from discord.ext import commands
from helpers import MESSAGES, ICON_URL, class_colors


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
        await ctx.send(MESSAGES['supported'])
    if ctx.message.content.split(
            '!classes ')[1].lower() not in MESSAGES['supported_list']:
        await ctx.send(MESSAGES['class_not_found'].format(
            ctx.message.content.split('!classes ')[1].lower()))


@classes.command(case_insensitive=True,
                 aliases=MESSAGES['supported_list'])
async def class_info(ctx):
    """Class info command return for a given class."""
    # Setup
    wait_message = await ctx.send(
        "```diff\n+ FETCHING INFO...\n```")
    info = None
    info_dict = {}
    invoked_call = ctx.invoked_with.lower()
    if invoked_call in ctx.command.aliases:
        info = DND.class_info(invoked_call).json()
    dice_count = info['class'][0]['hd']['number']
    dice_faces = info['class'][0]['hd']['faces']
    saving_throws = info['class'][0]['proficiency']

    # Build info_dict from Setup.
    info_dict['name'] = info['class'][0]['name']
    info_dict['source'] = info['class'][0]['source']
    info_dict['hit_dice'] = f"{dice_count}d{dice_faces}"
    info_dict['saving_throws'] = f"{saving_throws[0]}, {saving_throws[1]}"
    if invoked_call in ['wizard', 'sorcerer', 'monk']:
        info_dict['armor'] = "None"
        armor_string = "None"
    else:
        formatted_armor = []
        info_dict['armor'] = info[
            'class'][0]['startingProficiencies']['armor']
        for armor in info_dict['armor']:
            formatted_armor.append(armor.capitalize())
        armor_string = ", ".join(formatted_armor)
    info_dict['weapons'] = info['class'][0]['startingProficiencies']['weapons']
    info_dict['skills'] = info['class'][0]['startingProficiencies']['skills']
    skill_choice_count = info_dict['skills']['choose']
    skill_choices = info_dict['skills']['from']
    formatted_weapons = []
    for weapon in info_dict['weapons']:
        formatted_weapons.append(weapon.capitalize())
    skill_string = ", ".join(skill_choices)
    weapon_string = ", ".join(formatted_weapons)

    # Edit message and add embed info using info_dict
    embed = discord.Embed(
        title="from 5etools", url="https://5etools.com/classes.html",
        description=f"Source: {info_dict['source']}")
    embed.colour = class_colors[invoked_call]
    embed.set_author(
        name=f"{invoked_call}".capitalize(), url=f"{ICON_URL[invoked_call]}",
        icon_url=f"{ICON_URL['main_logo']}")
    embed.set_thumbnail(url=f"{ICON_URL[invoked_call]}")
    embed.add_field(
        name="Hit Dice: ", value=f"{info_dict['hit_dice']}", inline=False)
    embed.add_field(
        name="Proficiencies listed below:",
        value="----------------", inline=False)
    embed.add_field(
        name="Saving Throws: ", value=f"{info_dict['saving_throws'].upper()}",
        inline=True)
    embed.add_field(
        name="Armor: ", value=f"{armor_string}", inline=True)
    embed.add_field(
        name="Weapon(s):", value=f"{weapon_string}", inline=True)
    embed.add_field(
        name=f"Skills - Choose {skill_choice_count} skills from: ",
        value=(f"{skill_string}\n"
               "----------------"), inline=False)
    embed.set_footer(text="More info to come in the future.")
    await wait_message.edit(content="", embed=embed)

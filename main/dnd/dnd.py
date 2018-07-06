"""
Return responses data from the 5etools site.

Check them out at https://5etools.com/.
"""
import requests
from discord.ext import commands
from helpers import MESSAGES


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


@classes.error
async def classes_error_handler(ctx, error):
    """Local error handler for DND Bot class commands."""
    if (isinstance(
        error, commands.MissingRequiredArgument) or isinstance(
            error, commands.CommandNotFound)):
        await ctx.send(
            f'```diff\n- Invalid command: {ctx.message.content}\n```\n')


@classes.command(case_insensitive=True,
                 aliases=MESSAGES['supported_list'])
async def class_info(ctx):
    """Class info command return for a given class."""
    # Setup
    info = None
    info_dict = {}
    invoked_call = ctx.invoked_with.lower()
    import pdb; pdb.set_trace()
    if invoked_call not in MESSAGES['supported_list']:
        await ctx.send(
            f'**Error:**\n```\nClass name not found: {invoked_call}')
    if invoked_call in ctx.command.aliases:
        info = DND.class_info(invoked_call).json()
    else:
        await ctx.send(
            f'```css\n'
            f'Invalid class command: {ctx.message.content}\n'
            f'Please use the !classes command to see supported class '
            f'options.\n```\n')
    # discord.client.Client.get_all_channels()
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
    else:
        info_dict['armor'] = info[
            'class'][0]['startingProficiencies']['armor']
    info_dict['weapons'] = info['class'][0]['startingProficiencies']['weapons']
    info_dict['skills'] = info['class'][0]['startingProficiencies']['skills']
    skill_choice_count = info_dict['skills']['choose']
    skill_choices = info_dict['skills']['from']

    # Post built info_dict to chat.
    await ctx.send(
        f"```md\n[{info_dict['name']}]\n"
        f"# Source: {info_dict['source']}\n"
        f"# Hit Dice: {info_dict['hit_dice']}\n"
        f"# Proficiencies:\n1. Saving Throws: "
        f"{info_dict['saving_throws']} \n"
        f"2. Armor: {info_dict['armor']}\n3. Weapons: "
        f"{info_dict['weapons']}\n"
        f"# Skills - Choose {skill_choice_count} skills from:\n"
        f"# {skill_choices}\n```\n")
    await ctx.send('```bash\n"More info to come in the future!"\n```\n')

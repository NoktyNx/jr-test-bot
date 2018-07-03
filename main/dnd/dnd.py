"""
Return responses data from the 5etools site.

Check them out at https://5etools.com/.
"""
import requests
import discord
from discord.ext import commands
import dist
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
async def channels(ctx):
    """Get the list of channels from the current Discord server ("Guild")."""
    await ctx.send(
        'Set the main bot channel by using the command:\n'
        '`!channels setchannel name`\n'
        'name is the name of the channel (i.e. "general")')


def channels_list(context):
    """Called by other commands."""
    channels_list = []
    raw_channel_list = context.channel.guild.channels
    for channel in raw_channel_list:
        channels_list.append((channel.id, channel.name))
    return channels_list


@channels.command(case_insensitive=True, pass_context=True)
async def setchannel(ctx, arg):
    """Set the main bot channel for DND bot."""
    channels = channels_list(ctx)
    try:
        for (channel_id, channel_name) in channels:
            if channel_name == arg:
                ctx.bot_channel = channel_id
                import pdb; pdb.set_trace()
                # bot_channel = discord.Object(id=bot_channel_id)
                # await ctx.send(bot_channel, 'hello')
                await ctx.bot_channel.send('hello')
            else:
                await ctx.send(
                    f'Invalid Discord channel name specified: "{arg}"\n'
                    'Please try again. Valid channel names detected:\n'
                    f'{[channel[1] for channel in channels]}')
    except commands.errors.CommandInvokeError:
        return



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
    # discord.client.Client.get_all_channels()
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

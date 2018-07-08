"""
Rolls dice using the following command syntax:

/roll 1d6 where 1 is the number of dice, d6 is the sides of each dice.
Output in Discord chat: *User* rolled 1d6: *result*

Can do other rolls such as 1d20, 1d100, etc.

Also supports "bonuses" for rolls such as "1d6+50" where "+50" is the bonus
Can also do negative "penalties" the same way.
"""

import random
import re
import discord
from discord.ext import commands
from helpers import ICON_URL, ROLLER_MESSAGES, class_colors


class DiceRoller(object):
    """Handles the dice rolls."""
    def parse_roll(roll_arg, roll_bonus: bool):
        """Return a parsed regex object for doing a valid dice roll."""
        if roll_bonus:
            roll_string = re.search(
                r'^[\d*]{1,3}d[\d*]{1,3}[\+-][\d*]{1,3}$', roll_arg)
        else:
            roll_string = re.search(r'^[(\d*)]{1,3}d[\d*]{1,3}$', roll_arg)
        return roll_string

    def roll_dice(dice_count, dice_sides, bonus, splitter):
        """Roll a dice for a random outcome.

        rolled_dice is the returned dict.
        number_of_dice int: represents how many dice to roll.
        dice_sides int: represents how many sides on each die rolled.
        bonus int: represents how much to add/subtract from the roll.
        splitter string: denotes whether the bonus will be added or subtracted.
        """
        rolled_dice = {
            'roll_results': [],
            'individual_rolls': [],
            'total': 0,
            'bonus': 0,
        }
        for dice in range(0, dice_count):
            dice = random.randint(1, dice_sides)
            rolled_dice['roll_results'].append(dice)
        for dice in rolled_dice['roll_results']:
            rolled_dice['individual_rolls'].append((
                str(dice), f"({rolled_dice['roll_results'].count(dice)})"))
        unmodified_total = rolled_dice['total'] = int(sum(
            rolled_dice['roll_results']))
        if splitter == "+":
            rolled_dice['total'] = int(unmodified_total + bonus)
        elif splitter == "-":
            rolled_dice['total'] = int(unmodified_total - bonus)
        rolled_dice['bonus'] = bonus
        return rolled_dice


@commands.command(case_insensitive=True, pass_context=True)
async def roll(ctx, arg):
    """Roll dice."""
    # Setup, fail message if invalid.
    updated_arg = arg.lower()
    roll_bonus = '-' in updated_arg or '+' in updated_arg
    roll_string = DiceRoller.parse_roll(updated_arg, roll_bonus)
    try:
        valid_roll = roll_string.string
        roll_message = await ctx.send("```diff\n+ ROLLING...\n```")
        splitter = ''
        if '-' in valid_roll:
            splitter = '-'
        elif '+' in valid_roll:
            splitter = '+'
        dice_count = int(valid_roll.split('d')[0])
        if roll_bonus:
            dice_sides = int(valid_roll.split('d')[1].split(splitter)[0])
            dice_bonus = int(valid_roll.split('d')[1].split(splitter)[1])
        else:
            dice_sides = int(valid_roll.split('d')[1])
            dice_bonus = 0
        rolled_dice = DiceRoller.roll_dice(
            dice_count, dice_sides, dice_bonus, splitter)
        individual_dice_rolls = rolled_dice['individual_rolls']
        embed = discord.Embed(
            title="Results", description="----------------",
            colour=class_colors['dice_roller'])
        embed.set_author(
            name=(f"{ctx.message.author} rolled "
                  f"{dice_count}d{dice_sides}{splitter}{dice_bonus}"),
            icon_url=f"{ICON_URL['main_logo']}")
        embed.set_thumbnail(url=f"{ICON_URL['dice_roller']}")
        embed.add_field(
            name=f"Total (including bonus):", value=f"{rolled_dice['total']}",
            inline=True)
        embed.add_field(
            name="Individual Dice Rolls:",
            value=f"{individual_dice_rolls}", inline=True)
        await roll_message.edit(content="", embed=embed)
    except AttributeError:  # Fail if valid_roll isn't created
        await roll_message.edit(
            content=ROLLER_MESSAGES['invalid_roll'].format(arg))

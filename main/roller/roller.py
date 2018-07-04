"""
Rolls dice using the following command syntax:

/roll 1d6 where 1 is the number of dice, d6 is the sides of each dice.
Output in Discord chat: *User* rolled 1d6: *result*

Can do other rolls such as 1d20, 1d100, etc.
"""

import random
from discord.ext import commands


class DiceRoller(object):
    """Handles the dice rolls."""
    def roll_dice(number_of_dice, dice_sides):
        """Roll a dice for a random outcome.

        number_of_dice is a string representing how many dice to roll.
        dice_sides is a string representing how many sides on each die rolled.
        """
        dice_sides = int(dice_sides.replace("d", "").replace("D", ""))
        roll_results = []
        for dice in range(0, int(number_of_dice)):
            dice = random.randint(1, dice_sides)
            roll_results.append(dice)
        return roll_results


@commands.command(case_insensitive=True, pass_context=True)
async def roll(ctx, arg):
    """Roll dice."""
    import pdb; pdb.set_trace()
    await ctx.send("test")

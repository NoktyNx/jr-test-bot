"""Holds commands specific to the dice roller via the @commands decorator."""
from discord.ext import commands
from roller.roller import DiceRoller
from helpers import ROLLER_MESSAGES


@commands.command(case_insensitive=True, pass_context=True)
async def roll(ctx, arg):
    """Roll dice."""
    # Setup, fail message if invalid.
    roll_message = await ctx.send("```diff\n+ ROLLING...\n```")
    updated_arg = arg.lower()
    roll_bonus = '-' in updated_arg or '+' in updated_arg
    roll_string = DiceRoller.parse_roll(updated_arg, roll_bonus)

    try:
        valid_roll = roll_string.string
        dice_sides = 6
        dice_bonus = ''
        splitter = ''
        dice_bonus_string = ''
        individual_dice_rolls = ''

        if '-' in valid_roll:
            splitter = '-'
        elif '+' in valid_roll:
            splitter = '+'
        dice_count = int(valid_roll.split('d')[0])

        if not DiceRoller.blood_bowl_roll:
            if roll_bonus:
                dice_sides = int(valid_roll.split('d')[1].split(splitter)[0])
                dice_bonus = int(valid_roll.split('d')[1].split(splitter)[1])
            else:
                dice_sides = int(valid_roll.split('d')[1])
                dice_bonus = 0

            if dice_sides >= 101:
                raise AttributeError

            if dice_bonus >= 1:
                dice_bonus_string = dice_bonus

        rolled_dice = DiceRoller.roll_dice(
            dice_count, dice_sides, dice_bonus, splitter)
        individual_dice_rolls = ", ".join(rolled_dice['individual_rolls'])

        embed = DiceRoller.discord_embed(
            ctx, dice_count, dice_sides, splitter, dice_bonus_string,
            rolled_dice, individual_dice_rolls)
        await roll_message.edit(content="", embed=embed)
    except AttributeError:
        await roll_message.delete()
        await ctx.send(ROLLER_MESSAGES['invalid_roll'].format(arg))

"""
Rolls dice using the following command syntax:

/roll 1d6 where 1 is the number of dice, d6 is the sides of each dice.
Output in Discord chat: *User* rolled 1d6: *result*

Can do other rolls such as 1d20, 1d100, etc.

Also supports "bonuses" for rolls such as "1d6+50" where "+50" is the bonus
Can also do negative "penalties" the same way.

New: Users can now input "/roll 1dblock" to roll Blood Bowl block dice from
the Blood Bowl tabletop / video games. Obviously can increase the amount by
adding dice such as: "/roll 2dblock" or "/roll 3dblock"
"""

import random
import re
import discord
from helpers import (
    BLOOD_BOWL, BLOOD_BOWL_CASUALTIES, BLOOD_BOWL_INJURIES, DESCRIPTIONS,
    ICON_URL, INJURY_IMAGES, class_colors)


class DiceRoller(object):
    """Handles the dice rolls."""
    blood_bowl_roll = False

    def __generate_roll_results(dice_count, dice_sides):
        """Generate the roll results."""
        dice_list = []
        for dice in range(0, dice_count):
            dice = random.randint(1, dice_sides)
            dice_list.append(dice)
        return dice_list

    def __generate_individual_rolls(roll_results):
        """Generate individual dice roll counts."""
        dice_list = []
        for dice in roll_results:
            unique_dice = str(dice)
            dice_count = f"{roll_results.count(dice)}"
            if f"{unique_dice} ({dice_count})" not in dice_list:
                dice_list.append(f"{unique_dice} ({dice_count})")
        dice_list.sort(reverse=True)
        return dice_list

    def discord_embed(ctx, dice_count, dice_sides, splitter, dice_bonus_string,
                      rolled_dice, individual_dice_rolls):
        """Generate the embed message for Discord."""
        emoji_string = ""
        if DiceRoller.blood_bowl_roll:
            embed = discord.Embed(
                title='Block Rolls', description="----------------",
                colour=class_colors['dice_roller'])
            embed.set_author(
                name=(f"{ctx.message.author} rolled "
                      f"{dice_count} block dice."),
                icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=f"{ICON_URL['dice_roller']}")
            for result in rolled_dice['roll_results']:
                emoji_string += f' {BLOOD_BOWL[result]}'
            embed.add_field(
                name='Dice', value=emoji_string)
            DiceRoller.blood_bowl_roll = False
        else:
            embed = discord.Embed(
                title="Dice Rolls", description="----------------",
                colour=class_colors['dice_roller'])
            embed.set_author(
                name=(
                    f"{ctx.message.author} rolled "
                    f"{dice_count}d{dice_sides}{splitter}{dice_bonus_string}"),
                icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=f"{ICON_URL['dice_roller']}")
            embed.add_field(
                name=f"Total (including bonus)",
                value=f"{rolled_dice['total']}",
                inline=True)
            embed.add_field(
                name="Individual Dice Rolls",
                value=f"{individual_dice_rolls}", inline=True)
        return embed

    def injury_embed(ctx, injury_result):
        """Generate the Blood Bowl injury embed message for Discord."""
        casualty_string = ""
        if injury_result['casualty']:
            casualty_string = " Rolling casualty result."
        embed = discord.Embed(
            title='Injury Roll', description="----------------",
            colour=class_colors['dice_roller'])
        embed.set_author(
            name=f"{ctx.message.author} rolled 2d6 injury dice.",
            icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=f"{ICON_URL['dice_roller']}")
        embed.set_image(
            url=INJURY_IMAGES[injury_result['injury']])
        embed.add_field(
            name='Roll result',
            value=f"2d6 {injury_result['roll_results']}: "
                  f'"{injury_result["total"]}" total - Result: '
                  f"{injury_result['injury']}{casualty_string}")
        if casualty_string:
            embed.add_field(
                name='Casualty roll',
                value=f'1d6 (first digit): "{injury_result["d6"]}" \n'
                      f'1d8 (second digit): "{injury_result["d8"]}"\n'
                      f'Total: "{injury_result["d6"]}{injury_result["d8"]}"')
            embed.add_field(
                name='Result',
                value=f"{injury_result['casualty'][0]}: "
                      f"{injury_result['casualty'][1]}")
        else:
            embed.add_field(
                name='No casualty roll',
                value='Must roll a "Casualty" injury result for a casualty '
                      'roll.')
        return embed

    def parse_roll(roll_arg: str, roll_bonus=False):
        """Return a parsed regex object for doing a valid dice roll."""
        # Blood Bowl block dice rolls.
        if 'block' in str(roll_arg):
            roll_string = re.search(r'^[123]d(block)', roll_arg)
            DiceRoller.blood_bowl_roll = True
            return roll_string

        # Blood Bowl injury dice rolls.
        elif 'injury' in str(roll_arg):
            updated_arg = roll_arg[:6]
            roll_string = re.search(r'^(injury)', updated_arg)
            return roll_string

        # Normal dice rolls.
        if roll_bonus:
            roll_string = re.search(
                r'^[\d*]{1,3}d[\d*]{1,3}[\+-][\d*]{1,3}$', roll_arg)
        else:
            roll_string = re.search(r'^[(\d*)]{1,3}d[\d*]{1,3}$', roll_arg)
        return roll_string

    def roll_dice(dice_count: int, dice_sides: int, bonus: int,
                  splitter: str):
        """Roll a dice for a random outcome.

        rolled_dice is the returned dict.
        number_of_dice int: represents how many dice to roll.
        dice_sides int: represents how many sides on each die rolled. Gets
            typecast to a string if a Blood Bowl dice roll is made.
        bonus int: represents how much to add/subtract from the roll.
        splitter string: denotes whether the bonus will be added or subtracted.
        """
        rolled_dice = {
            'roll_results': [],
            'individual_rolls': [],
            'total': 0,
            'bonus': 0,
        }

        rolled_dice['roll_results'] = DiceRoller.__generate_roll_results(
            dice_count, dice_sides)
        rolled_dice[
            'individual_rolls'] = DiceRoller.__generate_individual_rolls(
                rolled_dice['roll_results'])
        unmodified_total = rolled_dice['total'] = int(sum(
            rolled_dice['roll_results']))

        if splitter == "+":
            rolled_dice['total'] = int(unmodified_total + bonus)
        elif splitter == "-":
            rolled_dice['total'] = int(unmodified_total - bonus)
        rolled_dice['bonus'] = bonus
        return rolled_dice

    def generate_injury():
        """Roll on the Blood Bowl injury and (possibly) casualty tables."""
        injury_result = DiceRoller.roll_injury(2, 6)
        injury_result['injury'] = BLOOD_BOWL_INJURIES[injury_result['total']]
        if injury_result['injury'] == 'Casualty':
            casualty_result = DiceRoller.roll_casualty()
            injury_result['casualty'] = BLOOD_BOWL_CASUALTIES[
                casualty_result['result']]
            injury_result['d6'] = casualty_result['d6']
            injury_result['d8'] = casualty_result['d8']
        return injury_result

    def roll_injury(dice_count: int, dice_sides: int):
        """Roll the Blood Bowl injury results."""
        injury_result = {
            'roll_results': [],
            'total': 0,
            'injury': '',
            'casualty': '',
            'd6': '',
            'd8': '',
        }

        injury_result['roll_results'] = DiceRoller.__generate_roll_results(
            dice_count, dice_sides)
        injury_result['total'] = int(sum(injury_result['roll_results']))
        return injury_result

    def roll_casualty():
        """Roll the Blood Bowl casualty results."""
        casualty_result = {
            'result': '',
            'd6': 0,
            'd8': 0,
        }
        first_digit = random.randint(1, 6)
        second_digit = random.randint(1, 8)
        casualty_result['result'] = int(f'{first_digit}{second_digit}')
        casualty_result['d6'] = first_digit
        casualty_result['d8'] = second_digit
        return casualty_result

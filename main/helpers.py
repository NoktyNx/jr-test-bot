"""Holds helper functions, data structures, and other tools."""

MESSAGES = {
    'supported':
        '```md\n# The following classes have information available:\n```\n'
        'Barbarian, Bard, Cleric, Druid, Fighter, Monk, Mystic, Paladin, '
        'Ranger, Rogue, Sorcerer, Warlock, Wizard\n'
        '```css\nTo obtain specific information about a class, use '
        '!classes classname (i.e. to get Barbarian info use '
        '!classes barbarian or !classes Barbarian)\n```\n',
    'supported_list': [
        'barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'mystic',
        'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard'],
    'class_not_found':
        '```diff\n- Error: D&D class name not found: '
        '"{0}"\n'
        '+ Use !classes to see a list of valid class choices.\n```\n',
}

ICON_URL = {
    'main_logo': 'https://i.imgur.com/xJcDRHb.png',
    'dice_roller': 'https://i.imgur.com/tR21xI6.png',
    'barbarian': 'https://i.imgur.com/xEd6t7Z.jpg',
    'bard': 'https://i.imgur.com/ZbMWWTo.jpg',
    'cleric': 'https://i.imgur.com/lUBwrgY.jpg',
    'druid': 'https://i.imgur.com/cdm0MUa.jpg',
    'fighter': 'https://i.imgur.com/rMTrANb.jpg',
    'monk': 'https://i.imgur.com/gxlitPZ.jpg',
    'mystic': 'https://i.imgur.com/3MaUYBU.jpg',
    'paladin': 'https://i.imgur.com/Q5VQy8f.jpg',
    'ranger': 'https://i.imgur.com/J7R3hW1.jpg',
    'rogue': 'https://i.imgur.com/GEt0Ccp.jpg',
    'sorcerer': 'https://i.imgur.com/no99l3U.jpg',
    'warlock': 'https://i.imgur.com/bxYboeI.jpg',
    'wizard': 'https://i.imgur.com/fBMUuwu.jpg',
}

class_colors = {
    'barbarian': 0xF4CCCC,  # Vanilla Ice
    'bard': 0x0000FF,  # Blue
    'cleric': 0xFFFFFF,  # White
    'druid': 0x38761D,  # Green
    'fighter': 0xFF0000,  # Red
    'monk': 0x000000,  # Orange
    'mystic': 0x45818E,  # Teal
    'paladin': 0xFFD966,  # Gold (Dandelion)
    'ranger': 0xBF9000,  # Dark Goldenrod
    'rogue': 0x000000,  # Black
    'sorcerer': 0xC27BA0,  # Pink (Hopbush)
    'warlock': 0x674EA7,  # Purple (Blue Marguerite)
    'wizard': 0x660000,  # Maroon
    'dice_roller': 0xCCCCCC,  # Light Grey
}


MONSTERS = {
    'Aarakocra': 0,
}


ROLLER_MESSAGES = {
    'invalid_roll':
        '```diff\n- Roll command invalid: "/roll {0}"\n```\n'
        '```md\n# Dice roll format is: \n'
        '/roll + amount of dice + dice sides +- bonus\n'
        'i.e.: /roll 1d6+5\n```\n'
        '```diff\n+ Discord caps messages to 2000 characters, so the roll '
        'results may have been too large to post.\n```\n',
    'success_result':
        "```md\n[Roll Results]\n```\n"
        "**Rolls:**\n {0}\n"
        "*Bonus to total*: {1}\n"
        "```diff\n+ Total: {2}\n```\n",
}

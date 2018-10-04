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

DESCRIPTIONS = {
    'badly_hurt': 'No long term effect',
    'broken_jaw': 'Miss next game.',
    'broken_ribs': 'Miss next game.',
    'fractured_arm': 'Miss next game.',
    'fractured_leg': 'Miss next game.',
    'smashed_hand': 'Miss next game.',
    'gouged_eye': 'Miss next game.',
    'groin_strain': 'Miss next game.',
    'pinched_nerve': 'Miss next game.',
    'damaged_back': "Niggling injury: adds 1 to all the player's injury rolls",
    'smashed_knee': "Niggling injury: adds 1 to all the player's injury rolls",
    'smashed_ankle': 'Loses 1 point in Movement Allowance.',
    'smashed_hip': 'Loses 1 point in Movement Allowance.',
    'fractured_skull': 'Loses 1 point in Armour Value.',
    'serious_concussion': 'Loses 1 point in Armour Value.',
    'broken_neck': 'Loses 1 point in Agility.',
    'smashed_collar_bone': 'Loses 1 point in Strength.',
    'dead': 'The player is dead; he is permanently removed from the team.',
    'stunned':
        'The player is knocked down. He will be unable to stand up until '
        'the next turn at a cost of 3 Movement points.',
    'ko':
        'The player leaves the pitch and ends up in the pit. On the next play '
        'there is one chance in two that he can go back on the pitch.',
    'casualty':
        'The player leaves the pitch for the rest of the match. He may miss '
        'the next match, lose statistic points and even die!'
}

INJURY_IMAGES = {
    f"Stunned: {DESCRIPTIONS['stunned']}": 'https://i.imgur.com/d6cqzLT.png',
    f"KO: {DESCRIPTIONS['ko']}": 'https://i.imgur.com/3M7zedR.png',
    f"Casualty: {DESCRIPTIONS['casualty']}": 'https://i.imgur.com/o9IO05y.png',
}

BLOOD_BOWL = {
    1: '<:push_back:496487887961849876>',
    2: '<:defender_stumbles:496487888041541653>',
    3: '<:attacker_down:496487887915843603>',
    4: '<:both_down:496487888075227156>',
    5: '<:defender_down:496487887987146753>',
    6: '<:push_back:496487887961849876>',
}

BLOOD_BOWL_INJURIES = {
    2: f"Stunned: {DESCRIPTIONS['stunned']}",
    3: f"Stunned: {DESCRIPTIONS['stunned']}",
    4: f"Stunned: {DESCRIPTIONS['stunned']}",
    5: f"Stunned: {DESCRIPTIONS['stunned']}",
    6: f"Stunned: {DESCRIPTIONS['stunned']}",
    7: f"Stunned: {DESCRIPTIONS['stunned']}",
    8: f"KO: {DESCRIPTIONS['ko']}",
    9: f"KO: {DESCRIPTIONS['ko']}",
    10: f"Casualty: {DESCRIPTIONS['casualty']}",
    11: f"Casualty: {DESCRIPTIONS['casualty']}",
    12: f"Casualty: {DESCRIPTIONS['casualty']}",
}

BLOOD_BOWL_CASUALTIES = {
    11: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    12: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    13: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    14: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    15: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    16: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    17: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    18: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    19: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    20: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    21: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    22: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    23: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    24: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    25: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    26: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    27: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    28: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    29: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    30: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    31: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    32: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    33: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    34: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    35: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    36: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    37: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    38: ['Badly hurt', DESCRIPTIONS['badly_hurt']],
    41: ['Broken jaw', DESCRIPTIONS['broken_jaw']],
    42: ['Broken ribs', DESCRIPTIONS['broken_ribs']],
    43: ['Fractured arm', DESCRIPTIONS['fractured_arm']],
    44: ['Fractured leg', DESCRIPTIONS['fractured_leg']],
    45: ['Smashed hand', DESCRIPTIONS['smashed_hand']],
    46: ['Gouged eye', DESCRIPTIONS['gouged_eye']],
    47: ['Groin strain', DESCRIPTIONS['groin_strain']],
    48: ['Pinched nerve', DESCRIPTIONS['pinched_nerve']],
    51: ['Damaged back', DESCRIPTIONS['damaged_back']],
    52: ['Smashed knee', DESCRIPTIONS['smashed_knee']],
    53: ['Smashed ankle', DESCRIPTIONS['smashed_ankle']],
    54: ['Smashed hip', DESCRIPTIONS['smashed_hip']],
    55: ['Fractured skull', DESCRIPTIONS['fractured_skull']],
    56: ['Serious concussion', DESCRIPTIONS['serious_concussion']],
    57: ['Broken neck', DESCRIPTIONS['broken_neck']],
    58: ['Smashed collar bone', DESCRIPTIONS['smashed_collar_bone']],
    61: ['Dead', DESCRIPTIONS['dead']],
    62: ['Dead', DESCRIPTIONS['dead']],
    63: ['Dead', DESCRIPTIONS['dead']],
    64: ['Dead', DESCRIPTIONS['dead']],
    65: ['Dead', DESCRIPTIONS['dead']],
    66: ['Dead', DESCRIPTIONS['dead']],
    67: ['Dead', DESCRIPTIONS['dead']],
    68: ['Dead', DESCRIPTIONS['dead']],
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
        '```diff\n- Roll command invalid: "/roll {0}"\n'
        '+ Please try again.\n'
        '[Current limit for dice sides is 100]\n'
        '[Blood Bowl block dice limit is 3dblock.]```\n'
}

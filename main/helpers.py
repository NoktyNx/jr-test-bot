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

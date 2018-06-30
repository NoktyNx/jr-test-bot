"""
Return responses data from the 5etools site.

Check them out at https://5etools.com/
"""
import requests
from helpers import CLASSES, MONSTERS


class DND(object):
    def __init__(self):
        """
        Init for the DND object.

        Starts requests.gets for json() data types and stores them as
        DND object attributes to manipulate in other methods that the
        Discord bot will use for chat commands

        Theoretical example command:
        Discord User: "!DND.monster.blinkdog"
        Bot response:
            Name: "Blink Dog"
            Type: "Medium Fey"
            Alignment: "Lawful Good"
            Source: "Monster Manual"
            Armor Class: "13"
            etc.
        """
        super().__init__()
        self.class_json = requests.get(
            "https://5etools.com/data/classes.json?ver=1.53.1")
        self.monster_json = requests.get(
            "https://5etools.com/data/bestiary/bestiary-mm.json?ver=1.53.1")

    def classes(self, class=""):
        """
        Class request information.

        class is a string representing the desired class data.
        info is a string representing the desired class information,
            if specified.
        """
        self.class_json.json()['class'][[CLASSES['Barbarian']]['name']  # Barbarian
        self.class_json.json()['class'][[CLASSES[class]]['name']  # "Bard"
        self.class_json.json()['source']  # "PHB"
        #  etc.

    def monsters(self, monster="", info=""):
        """
        Monster request information.

        monster is a string representing the desired monster data.
        info is a string repreenting the desired monster information,
            if specified.
        """
        self.monster_json()['monster'][MONSTERS['Aarakocra']['name']
                                       # Aarakocra

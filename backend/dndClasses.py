import math


class Spell:
    def __init__(self):
        self.name = ""
        self.level = ""
        self.classes = ""
        self.time = ""
        self.range = ""
        self.duration = ""
        self.components =""
        self.ritual =""
        self.school = ""
        self.text  =""


class Item:
    def __init__(self):
        self.name = ""
        self.detail =""
        self.weight = ""
        self.value = ""
        self.text = ""




class Feature:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc


class Char:
    def __init__(self,existingChr = None):
        self.userID = "" if existingChr == None else existingChr["userID"]
        self.linkedGame = "" if existingChr == None else existingChr["linkedGame"]
        self.Cname = "" if existingChr == None else existingChr["Cname"]
        self.base = {
            "class":"",
            "level":0,
            "background":"",
            "race":"",
            "Pname":"",
            "alignment":"",
            "hp":{
                "value":0,
                "min":0,
                "max":0,
                "temporary":0,
                "hitDice": {
                    "sides":0,
                    "num":0
                }
            },
            "speed":{
                "land":0,
                "flying":0,
                "swimming":0,
                "climbing":0
            },
            "initiative":0,
            "ac":0,
            "deathSaves":{
                "successes":0,
                "failures":0
            },
            "passivePerception":0
        } if existingChr == None else existingChr["base"]
        self.ability = {
            "str":0,
            "dex":0,
            "con":0,
            "int":0,
            "wis":0,
            "chr":0,
            "savingThrows":{
                "str":False,
                "dex":False,
                "con":False,
                "int":False,
                "wis":False,
                "chr":False
            },
            
        } if existingChr == None else existingChr["ability"]
        self.skills = {
            "acrobatics":{
                "hasSkill":0,
                "label":"acrobatics",
                "modifier":0,
                "from":"dex"
            },
            "animalHandling":{
                "hasSkill":0,
                "label":"animal handling",
                "modifier":0,
                "from":"wis"
            },
            "arcana":{
                "hasSkill":0,
                "label":"arcana",
                "modifier":0,
                "from":"int"
            },
            "athletics":{
                "hasSkill":0,
                "label":"athletics",
                "modifier":0,
                "from":"str"
            },
            "deception":{
                "hasSkill":0,
                "label":"deception",
                "modifier":0,
                "from":"chr"
            },
            "history":{
                "hasSkill":0,
                "label":"history",
                "modifier":0,
                "from":"int"
            },
            "insight":{
                "hasSkill":0,
                "label":"insight",
                "modifier":0,
                "from":"wis"
            },
            "intimidation":{
                "hasSkill":0,
                "label":"intimidation",
                "modifier":0,
                "from":"chr"
            },
            "investigation":{
                "hasSkill":0,
                "label":"investigation",
                "modifier":0,
                "from":"int"
            },
            "medicine":{
                "hasSkill":0,
                "label":"medicine",
                "modifier":0,
                "from":"wis"
            },
            "nature":{
                "hasSkill":0,
                "label":"nature",
                "modifier":0,
                "from":"int"
            },
            "perception":{
                "hasSkill":0,
                "label":"perception",
                "modifier":0,
                "from":"wis"
            },
            "performance":{
                "hasSkill":0,
                "label":"performance",
                "modifier":0,
                "from":"chr"
            },
            "persuasion":{
                "hasSkill":0,
                "label":"persuasion",
                "modifier":0,
                "from":"chr"
            },
            "religion":{
                "hasSkill":0,
                "label":"religion",
                "modifier":0,
                "from":"int"
            },
            "slightOfHand":{
                "hasSkill":0,
                "label":"slight of hand",
                "modifier":0,
                "from":"dex"
            },
            "stealth":{
                "hasSkill":0,
                "label":"stealth",
                "modifier":0,
                "from":"dex"
            },
            "survival":{
                "hasSkill":0,
                "label":"survival",
                "modifier":0,
                "from":"wis"
            }
        } if existingChr == None else existingChr["skills"]
        self.biography = {
            "appearance":{
                "age":0,
                "height":0,
                "weight":0,
                "eyes":"",
                "skin":"",
                "hair":"",
                "description":"",
                "size":""
            },
            "portrait":"",
            "backstory":"",
            "notes":"",
            "personality":{
                "personalityTraits":"",
                "ideals":"",
                "bonds":"",
                "flaws":""
            },
            "people":{
                "allies":"",
                "enemies":"",
                "organizations":"",
                "other":""
            }
        } if existingChr == None else existingChr["biography"]
        self.features = {
            "profeciencies":[],
            "languages":[],
            "classFeatures":[],
            "raceFeatures":[],
            "feats":[],
            "otherFeats":[],
            "otherProfs":[],
            "resistances":[],
            "immunities":[],
            "vulnerabilities":[]
        } if existingChr == None else existingChr["features"]
        self.inventory = {
            "money":{
                "cp":0,
                "sp":0,
                "ep":0,
                "gp":0,
                "pp":0
            },
            "equipment":{
            "weapons":[],
            "armor":[],
            "consumables":[],
            "magical":[],
            "important":[],
            "misc":[],
            "treasure":[]
            }

        } if existingChr == None else existingChr["inventory"]
        self.spells = {
            "level":{
            "cantrips":[],
            "level1":[],
            "level2":[],
            "level3":[],
            "level4":[],
            "level5":[],
            "level6":[],
            "level7":[],
            "level8":[],
            "level9":[]
            },
            "spellBase":{
                "spellClass":"",
                "ability":"",
                "saveDC":0,
                "bonus":0
            },
            "spellSlots":{
            "level1":{
            "value":0,
            "max":0
            },
            "level2":{
            "value":0,
            "max":0
            },
            "level3":{
            "value":0,
            "max":0
            },
            "level4":{
            "value":0,
            "max":0
            },
            "level5":{
            "value":0,
            "max":0
            },
            "level6":{
            "value":0,
            "max":0
            },
            "level7":{
            "value":0,
            "max":0
            },
            "level8":{
            "value":0,
            "max":0
            },
            "level9":{
            "value":0,
            "max":0
            }
            }
        } if existingChr == None else existingChr["spells"]
import math


class Spell:
    def __init__(self):
        self.name = ""
        self.level = ""
        self.classes = ""
        self.time = ""
        self.range = ""
        self.duration = ""
        self.components = ""
        self.ritual = ""
        self.school = ""
        self.text  = ""


class Item:
    def __init__(self,name,detail,weight, value, text):
        self.name = name
        self.detail =detail
        self.weight = weight
        self.value = value
        self.text = text




class Feature:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc


class Char:
    def __init__(self,existingChr = None):
        self.userID = "" if existingChr == None else existingChr["userID"]
        self.linkedGame = "" if existingChr == None else existingChr["linkedGame"]
        self.base = {
            "name":"",
            "class":"",
            "level":0,
            "background":"",
            "race":"",
            "playername":"",
            "alignment":"",
            "ac":0,
            "passiveperception":0,
            "initiative":0,
            "hp":{
                "value":0,
                "max":0,
                "temporary":0,
                "hitdie": 0
            },
            "speed":{
                "land":0,
                "flying":0,
                "swimming":0,
                "climbing":0
            },
            "deathsaves":{
                "successes":0,
                "failures":0
            }
        } if existingChr == None else existingChr["base"]
        self.ability = {
            "str":{
                "value":0,
                "saveingThrow":False,
                "modifier":0,
            },
            "dex":{
                "value":0,
                "saveingThrow":False,
                "modifier":0,
            },
            "con":{
                "value":0,
                "saveingThrow":False,
                "modifier":0,
            },
            "int":{
                "value":0,
                "saveingThrow":False,
                "modifier":0,
            },
            "wis":{
                "value":0,
                "saveingThrow":False,
                "modifier":0,
            },
            "chr":{
                "value":0,
                "saveingThrow":False,
                "modifier":0,
            }
            
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
            "backstory":"",
            "notes":"",
            "personality":{
                "personalityTraits":"",
                "ideals":"",
                "bonds":"",
                "flaws":""
            },
            "connections":{
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
            "bag":{
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
            "slots":{
            "cantrips":{
                "spells":[],
                "value":0,
                "max":0
                },
            "level1":{
                "spells":[],
                "value":0,
                "max":0
                },
            "level2":{
                "spells":[],
                "value":0,
                "max":0
                },
            "level3":{
                "spells":[],
                "value":0,
                "max":0
                },
            "level4":{
                "spells":[],
                "value":0,
                "max":0
                },
            "level5":{
                "spells":[],
                "value":0,
                "max":0
                },
            "level6":{
                "spells":[],
                "value":0,
                "max":0
                },
            "level7":{
                "spells":[],
                "value":0,
                "max":0
                },
            "level8":{
                "spells":[],
                "value":0,
                "max":0
                },
            "level9":{
                "spells":[],
                "value":0,
                "max":0
                }
            },
            "spellBase":{
                "spellClass":"",
                "ability":"",
                "saveDC":0,
                "bonus":0
            }
        } if existingChr == None else existingChr["spells"]

    def calcMods(self):
        for attrib in self.ability:
            self.ability[attrib]["modifier"] = math.floor((self.ability[attrib]["value"] - 10)/2)
            if self.ability[attrib]["saveingThrow"]:
                self.ability[attrib]["modifier"] += math.ceil(1 + 1/4 * self.base["level"])
        for skill in self.skills:
            self.skills[skill]["modifier"] = self.skills[skill]["hasSkill"] * math.ceil(1 + 1/4 * self.base["level"]) + math.floor((self.ability[self.skills[skill]["from"]]["value"])/2)
        
    
    def addItem(self, item:dict, destination:str):
        item["amount"] = 1
        self.inventory["bag"][destination].append(item)
    
    def addSpell(self, spell:dict, slot:str):
        self.spells["slots"][slot]["spells"].append(spell)

    def addfeature(self, feature:dict, destination:str):
        self.features[destination].append(feature)
    




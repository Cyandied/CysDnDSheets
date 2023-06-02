from os import listdir, mkdir
from os.path import join
from backend.dndClasses import *
import json

def viewSheet(form, pc, spells, items, jsonnam, folder):

    with open(f'{folder}/{jsonnam}.json', "w") as f:
        f.write(json.dumps(pc.__dict__))

def editSheet(form, pc, spells, items, jsonnam, folder):

    with open(f'{folder}/{jsonnam}.json', "w") as f:
        f.write(json.dumps(pc.__dict__))





def makeNewJson(jsonNam, id,folder):
    PCs = [] 
    user_folders = listdir("PCs")
    if id not in user_folders:
        mkdir(join("PCs",id))
    for pc in listdir(folder):
        PCs.append(pc.split(".")[0])
    if jsonNam not in PCs:
        pc = Char().__dict__
        pc["userID"] = id
        with open(f'{folder}/{jsonNam}.json', "x") as f:
            f.write(json.dumps(pc))
    return
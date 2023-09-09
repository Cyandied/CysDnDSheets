from os import listdir, mkdir
from os.path import join
from backend.dndClasses import *
import json
from flask import flash
from pocketbase import PocketBase

client = PocketBase("http://127.0.0.1:8090")

def makeNumber(to_try):
    try:
        value = int(to_try)
    except:
        value = 0
        flash("It seems one or more things that were supposed to be a number, was not, the offending inputs will be set to 0")
    return value

def viewSheet(form, sheet_id:str, pc:Char):
    if "button" in form:
        if form["button"] == "link-game":
            if form["link-game"]:
                client.collection("sheets").update(sheet_id, {
                    "game_id":form["link-game"],
                    "sheet_json":pc.__dict__
                })
                pc.linkedGame = form["link-game"]
                flash("game linked, your DM now has acess to this sheet")
            else:
                flash("please enter a valid game id, ask your dm for it!")
        elif form["button"] == "unlink-game":
            client.collection("sheets").update(sheet_id, {
                "game_id":"",
                "sheet_json":pc.__dict__
            })
            pc.linkedGame = ""
            flash("game unlinked, your DM no longer has acess to this sheet")
        else:
            client.collection("sheets").update(sheet_id, {
                "sheet_json":pc.__dict__
            })

def editSheet(form, pc:Char, spells, items, sheet_id):

    #base____________________________________________________________________________________________________________
    for part in pc.base:
        if part not in ["hp","speed","deathsaves"]:
            if part in ["level","ap","passivePerception","initiative"]:
                pc.base[part] = makeNumber(form[part])
            else: pc.base[part] = form[part]
    pc.base["hp"]["value"] = form["hp.value"]
    pc.base["hp"]["max"] = form["hp.max"]
    pc.base["hp"]["temporary"] = form["hp.temporary"]
    pc.base["hp"]["hitdie"] = form["hp.hitdie"]

    pc.base["deathsaves"]["failures"] = form["deathsaves.failures"]
    pc.base["deathsaves"]["successes"] = form["deathsaves.successes"]

    for terrain in pc.base["speed"]:
        pc.base["speed"][terrain] = form[f'speed.{terrain}']

    #overview____________________________________________________________________________________________________________
    for ability in pc.ability:
        value = makeNumber(form[f'{ability}.value'])
        pc.ability[ability]["value"] = value
        if f'{ability}.saveingThrow' in form:
            pc.ability[ability]["saveingThrow"] = True
        else:
            pc.ability[ability]["saveingThrow"] = False
    for skill in pc.skills:
        pc.skills[skill]["hasSkill"] = int(form[f'{skill}.hasSkill'])

    pc.calcMods()

    #inventory____________________________________________________________________________________________________________
    for money in pc.inventory["money"]:
        pc.inventory["money"][money] = form[money]
    
    #spells____________________________________________________________________________________________________________
    for base in pc.spells["spellBase"]:
        pc.spells["spellBase"][base] = form[base]

    #biography__________________________________________________________________________________________________________
    for category in pc.biography:
        if category not in ["notes","backstory"]:
            for attrib in pc.biography[category]:
                pc.biography[category][attrib] = form[attrib]
        else:
            pc.biography[category] = form[category]
        



    if "button" in form:
        #overview____________________________________________________________________________________________________________
        if "add-new-feature" in form["button"]:
            category, _ = form["button"].split(".")
            feature = Feature(form[f'new-feature-title.{category}'],form[f'new-feature-desc.{category}'])
            pc.addfeature(feature.__dict__, category)
        elif "delete-feature" in form["button"]:
            category, index, _ = form["button"].split(".")
            pc.features[category].pop(int(index)-1)

        #inventory____________________________________________________________________________________________________________
        elif "delete-item" in form["button"]:
            category, index, _ = form["button"].split(".")
            pc.inventory["bag"][category].pop(int(index)-1)
        elif "add-exsisting-item" in form["button"]:
            category = form["add-to-category-item"]
            index,_ = form["button"].split(".")
            item = items[int(index)-1]
            print(item, category)
            pc.addItem(item,category)
        elif "add-new-item" in form["button"]:
            category = form["add-to-category-item"]
            item = Item(form["name.new-item"],form["detail.new-item"],form["weight.new-item"],form["value.new-item"],form["text.new-item"])
            pc.addItem(item.__dict__, category)
        #spells__________________________________________________________________________________________________________________________
        elif "delete-spell" in form["button"]:
            category,index,_ = form["button"].split(".")
            pc.spells["slots"][category]["spells"].pop(int(index)-1)
        elif "add-exsisting-spell" in form["button"]:
            category = form["add-to-category-spell"]
            index,_ = form["button"].split(".")
            spell = spells[int(index)-1]
            pc.addSpell(spell,category)
        elif "add-new-spell" in form["button"]:
            category = form["add-to-category-spell"]
            spell = Spell().__dict__
            for attrib in spell:
                spell[attrib] = form[f'{attrib}.new-spell']
            spells.append(spell)

        #link game_____________________________________________________________________________________________________________________
        elif form["button"] == "link-game":
            if form["link-game"]:
                pc.linkedGame = form["link-game"]
                flash("game linked, your DM now has acess to this sheet")
            else: flash("Please be sure to paste a valid game id!")
        elif form["button"] == "unlink-game":
            pc.linkedGame = ""
            flash("game unlinked, your DM no longer has acess to this sheet")

    client.collection("sheets").update(sheet_id, {
        "sheet_json":pc.__dict__
    })

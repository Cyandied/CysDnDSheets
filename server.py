import json
from flask import Flask, render_template, request, redirect, url_for, session, flash
from os import listdir, remove
from os.path import isfile, join
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import requests as req

from backend.classes import *
from backend.dndClasses import *
from backend.functions import *

#Start server:
#flask --app server run --debug

PBURL = "http://127.0.0.1:8090/api/collections"

app = Flask(__name__, static_url_path="", static_folder="static", template_folder="html")

app.secret_key = "i/2r:='d8$V{[:gHm5x?#YBB-D-6)N"

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    users = req.get(f'{PBURL}/users/records?expand=user_packs(user_id).pack_id').json()["items"]
    for user in users:
        packs = []

        if "expand" in user:
            for entry in user["expand"]["user_packs(user_id)"]:
                packs.append(entry["expand"]["pack_id"]["name"])

        email = None
        if "email" in user:
            email = user["email"]

        if user_id == user["id"]:
            return User(user["username"], email, user["role"],[], user["id"], packs, user["secret"])
        
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        response = req.post(f'{PBURL}/users/auth-with-password?expand=user_packs(user_id).pack_id',json = {
            "identity" : request.form["user"],
            "password" : request.form["pass"]
        }).json()

        verified_user = False
        if "code" not in response:
            response = response["record"]
            packs = []
            user_games = {}

            if "expand" in response:
                for entry in response["expand"]["user_packs(user_id)"]:
                    packs.append(entry["expand"]["pack_id"]["name"])

            user = response

            if user["role"] in ["admin","dm"]:
                response_for_games = req.get(f'{PBURL}/users/records/{user["id"]}?expand=user_games(user_id).game_id').json()
                if "expand" in response:
                    for game in response_for_games["expand"]["user_games(user_id)"]:
                        game = game["expand"]["game_id"]
                        user_games[game["name"]] = game["id"]
            email = None
            if "email" in user:
                email = user["email"]

            verified_user = User(user["username"], email, user["role"],user_games, user["id"],packs, user["secret"])
        
        if verified_user:
            session["user"] = verified_user.__dict__
            session["hw"] = None
            login_user(verified_user)
            flash(f'sucessfully logged in! Welcome {session["user"]["name"]}')
            return redirect(url_for("home"))
        
        else:
            flash("Sorry, check if the username and password is correct.")
    
    
    return render_template("index.html")

@app.route("/home", methods=["GET", "POST"])
@login_required
def home():
    session["last-tab"] = "overview"
    PCs = []
    if session["user"]["id"] in listdir("PCs"):
        for jsonNam in listdir(f'PCs/{session["user"]["id"]}'):
            with open(f'PCs/{session["user"]["id"]}/{jsonNam}', 'r') as f:
                pc = Char(existingChr=json.loads(f.read()))
            if pc.userID == session["user"]["id"]:
                PCs.append([f'{pc.userID}~{jsonNam.split(".")[0]}',"own"])
    if session["user"]["id"] in listdir("PCs") and session["user"]["role"] in ["dm","admin"]:
        for userfolder in listdir("PCs"):
            for jsonNam in listdir(f'PCs/{userfolder}'):
                with open(f'PCs/{userfolder}/{jsonNam}', 'r') as f:
                    pc = Char(existingChr=json.loads(f.read()))
                if pc.linkedGame in session["user"]["games"].values():
                    index = list(session["user"]["games"].values()).index(pc.linkedGame)
                    PCs.append([f'{pc.userID}~{jsonNam.split(".")[0]}',list(session["user"]["games"])[index]])

    if request.method == "POST":

        if request.form["sheet-name"]:
            session["relavant_userfolder"] = session["user"]["id"]
            return redirect(url_for(f'sheet',jsonNam = request.form["sheet-name"].replace(" ","-")))
        elif "redirect-to" in request.form:
            if request.form["redirect-to"] == "load-sheet":
                if "sheets" in request.form:
                    user_folder, jsonNam = request.form["sheets"].split("~")
                    session["relavant_userfolder"] = user_folder
                    return redirect(url_for(f'sheet',jsonNam = jsonNam))
                else: flash("Seems you forgot to select a character sheet to laod :(")
    return render_template("home.html", user = session["user"], PCs = PCs)

@app.route(f'/sheet/<jsonNam>', methods=["GET", "POST"])
@login_required
def sheet(jsonNam):
    user_folder = join("PCs", session["relavant_userfolder"])
    makeNewJson(jsonNam, session["user"]["id"],user_folder)
    with open(f'{user_folder}/{jsonNam}.json', 'r') as f:
        pc = Char(existingChr=json.loads(f.read()))
    with open("itemsSpellsFeatures/spells.json","r") as f:
        spellsMaster = json.loads(f.read())
    with open("itemsSpellsFeatures/items.json","r") as f:
        itemsMaster = json.loads(f.read())

    form = request.form

    if request.method == "POST":
        session["last-tab"] = form["last-tab"]
        viewSheet(form, pc, spellsMaster, itemsMaster, jsonNam, user_folder)

        if "button" in form:
            if form["button"] == "edit-mode":
                return redirect(url_for(f'sheet_edit',jsonNam = jsonNam))
            if form["button"] == "home":
                return redirect(url_for("home"))

    return render_template("parts/sheet.html", pc = pc, spells = spellsMaster, items = itemsMaster, user = session["user"], last_tab = session["last-tab"], editmode = False)

@app.route(f'/sheet/<jsonNam>/edit_mode', methods=["GET", "POST"])
@login_required
def sheet_edit(jsonNam):
    user_folder = join("PCs", session["user"]["id"])
    with open(f'{user_folder}/{jsonNam}.json', 'r') as f:
        pc = Char(existingChr=json.loads(f.read()))
    with open("itemsSpellsFeatures/spells.json","r") as f:
        spellsMaster = json.loads(f.read())
    with open("itemsSpellsFeatures/items.json","r") as f:
        itemsMaster = json.loads(f.read())

    form = request.form
    
    if request.method == "POST":
        session["last-tab"] = form["last-tab"]
        editSheet(form, pc, spellsMaster, itemsMaster, jsonNam, user_folder)
    
        if "button" in form:
            if form["button"] == "back":
                return redirect(url_for(f'sheet',jsonNam = jsonNam))

        
    return render_template("parts/sheet_edit_mode.html", pc = pc, spells = spellsMaster, items = itemsMaster, last_tab = session["last-tab"], editmode = True)


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash(f'You are now logged out! Hope to see you soon, {session["user"]["name"]}')
    session["user"] = None
    session["hw"] = None
    return redirect(url_for("login"))

# if __name__ == "__main__":
#     app.run(debug = True)
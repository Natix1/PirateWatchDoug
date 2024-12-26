# pwdlib stands for pirate watch doug library
# didnt want to write it all out in file name
# + im not creative
# By the way the promised rewrite I did in release v0.0.1 - I decided to get to it

import discord
from pathlib import Path
import logging
from json import load, dump
from os import getenv
from dotenv import load_dotenv
from datetime import datetime, timezone

# VARS

sequenceProxy = discord.utils.SequenceProxy
defaultPirateMessage = """
Yo, so like, pirating is totally not the vibe, fam. 
It's lowkey stealing and messes up the game for devs who worked hard, ya know? 
If you're out here downloading sketchy stuff, you're risking your device, too. 
Like, you don't wanna catch a virus or get your account hacked, right? 
Plus, it's straight-up illegal, bro, and we don’t need that smoke. 
Just support the creators, buy the thing, and keep it 100. 
Don’t be a pirate, be a good homie.
https://tenor.com/view/hop-on-spacewar-spacewar-hop-on-hop-space-gif-15791507099589222017
https://tenor.com/view/memories-gif-21184195
ᵗʰᶦˢ ᵐᵉˢˢᵃᵍᵉ ʷᵃˢ ᵃᵘᵗᵒᵐᵃᵗᶦᶜᵃˡˡʸ ᵃⁿᵈ ᵖʳᵒᵍʳᵃᵐᵃᵗᶦᶜᵃˡˡʸ ˢᵉⁿᵗ ᵇʸ ᴾᶦʳᵃᵗᵉᵂᵃᵗᶜʰᴰᵒᵘᵍ
"""

defaultConfigVars = {
    "prefix": "!",
    "scanCommand": "scan",
    "allowedUserIds": [1]
}

def initChecks() -> None:
    srcDir = Path("./src/")
    if not srcDir.is_dir():
        logging.critical("Make sure you run this file from the root directory of this project (not ./src/)")
        print("Make sure you run this file from the root directory of this project (not ./src/)")
        exit(1)
        
        
    filedotenv = Path(".env")
    if not filedotenv.is_file():
        logging.critical(".env file not found; put your token using this format: TOKEN=(yourtokenhere) (not src!)")
        with open(".env", "w") as w:
            w.write("")
            
        exit(1)
    
    HoP = Path("./src/hall_of_pirates.json")
    if not HoP.is_file():
        logging.warning("hall_of_pirates.json not found: Created it")
        with open("./src/hall_of_pirates.json", "w") as w:
            dump([], w, indent=2)

        
    cfg = Path("./src/config.json")
    if not cfg.is_file():
        logging.warning("config.json not found: Created it")
        with open("./src/config.json", "w") as w:
            dump(defaultConfigVars, w, indent=2)
        
        
    
    msgFile = Path("./src/piracy_message.txt")
    if not msgFile.is_file():
        logging.warning("piracy_message.txt not found: Created it with default content")
        with open("./src/piracy_message.txt", "w") as w:
            w.write(defaultPirateMessage)
            
    return


def getToken() -> str:
    load_dotenv(".env")
    TOKEN = getenv("TOKEN")
    if not TOKEN:
        print("No token provided!")
        logging.critical("No TOKEN provided: put your token using this format: TOKEN=(yourtokenhere)")
        exit(1)
        
    TOKEN = TOKEN.replace('"', '')
    
    return TOKEN

def getPirateMessage() -> str:
    with open("./src/piracy_message.txt", "r") as r:
        msg = r.read()
    
    
    if msg == "":
        logging.critical("No message specified in piracy_message.txt")
        exit(1)
    
    msg = msg.strip()
    return msg


def parseFromConfig(value: str) -> dict:
    with open("./src/config.json", "r") as r:
        dictCfg = load(r)
        
    return dictCfg[value]

def spacewarDetection(user: discord.Member) -> bool:
    for activity in user.activities:
        if not isinstance(activity, discord.Game):
            continue
        
        if activity.name == "Spacewar":
            print("Spacewar detected")
            return True
        
    return False

def timenow() -> str:
    current_utc_time = datetime.now(timezone.utc)
    iso_utc_time = current_utc_time.isoformat()
    
    return iso_utc_time

def logPirate(user: discord.Member) -> None:
    with open("./src/hall_of_pirates.json", "r") as r:
        HoC: list = load(r)
    
    # Move to a set() for faster operation
    
    for i in HoC:
        if HoC[i]["uid"] == user.id:
            HoC[i]["times"] += 1
            break
        
    HoC.append({
        "uid": user.id,
        "name": user.name,
        "displayname": user.display_name,
        "times": 1
    })
    
    with open("./src/hall_of_pirates.json", "w") as w:
        dump(HoC, w, indent=2)
    
    return


if __name__ == "__main__":
    initChecks()
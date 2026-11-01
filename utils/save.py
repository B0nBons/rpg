import json
import os
# literally forgot ts got imported

# ok so ive never had to code in saving before so this is probably gonna be a hell of a ride
SAVE_SKELETON = {
    "player_info" : {
        "name" : "None", # so it erred on here when i ran so maybe none isnt allowed ??? changed it to text
        "total_xp" : 0,
        "level" : 1,
        "gold" : 0},

    "main_story" : {
        "Mirexio, The Hated" : "not_done",
        "Elysia, The Explorer" : "not_done",
        "Twilia, The Lost" : "not_done", 
        "Nemaro, The Seeker" : "not_done",
        "Klysari, The Queen" : "not_done",
        "Rumento, The Traitor" : "not_done",
        "Mirexio, The Storyteller" : "not_done"
    },
    "side_quests" : {
        "A Warrior's Guide To... Shopkeeping?" : "not_done",
        "A g-g-ghost?!" : "not-done"
    },
    "character_quests" : {
        "Help Wanted, Please" : "not_done", # triton act 1
        "More Help Wanted, Please" : "not_done",
        "Help Needed, Please" : "not_done",
        "A Fishy Surprise" : "not_done", # perlos act1
        "Fish Outta Water -- HELP!!!" : "not_done",
        "O Flying Fish!": "not_done",
        "The Price of Love" : "not_done", # duffaye (he stepped on his sheeps foot or som)
        "The Importance of Love" : "not_done",
        "I'm Sorry, Sheperus!!!" : "not_done",
        "Request: Preventing Disaster" : "not_done", # march
        "Request: Facing Disaster" : "not_done",
        "Request: Removal of Disaster" : "not_done",
        "EASY GOLD OPPORTUNITY" : "not_done", # serlarp ofc
        "VERY EASY GOLD JOB (HIGH PAYOUT)" : "not_done",


    },
    "forge" : {
        "status" : "empty", # can be empty, forging(??) or done
        "item" : None,
        "battles_until_done" : 0
    }
}

# yeah so i overcomplicated it, i just need to make a "basic" save yk??


# ONLY this func is ai, solely because after packaging, the game threw a bunch of permission errors
def good_save_path():
    home_dir = os.path.expanduser("~")
    game_folder = os.path.join(home_dir, ".my_rpg_game")
    
    # Create the folder if it doesn't exist yet
    if not os.path.exists(game_folder):
        os.makedirs(game_folder)
        
    return os.path.join(game_folder, "save.json")

def new_save():
    savefile = {}
    for val, item in SAVE_SKELETON.items():
        savefile[val] = item.copy()
    return savefile

def save_game(save_data, file_loc="data/save.json"):
    file_loc = good_save_path()
    location = os.path.dirname(file_loc)
    if location and not os.path.exists(location):
            os.makedirs(file_loc)
    with open(file_loc, "w") as f:
        json.dump(save_data, f)
        # yeah so idfk how to make this work guys pls HELP

def load_game(file_loc="data/save.json"): # this probably does NOT work right
    file_loc = good_save_path()
    if not os.path.exists(file_loc) or os.path.getsize(file_loc) == 0:
        NEW_save = new_save()
        save_game(NEW_save, file_loc)
    try:
        with open(file_loc, 'r') as f:
            load = json.load(f)

        for area in SAVE_SKELETON:
            if area not in load:
                load[area] = SAVE_SKELETON[area].copy()
            else:
                for inside in SAVE_SKELETON[area]:
                    if inside not in load[area]:
                        load[area][inside] = SAVE_SKELETON[area][inside]
        
        return load
    except Exception as e:
        print("Error reading savefile. " + str(e))
        # OK I MAY HAVE FIGURED IT OUT (!!!) 
        # when loading the file, it might not even exist and so itll error i think maybe idk
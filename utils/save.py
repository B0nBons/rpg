import json
import os

# ok so ive never had to code in saving before so this is probably gonna be a hell of a ride
SAVE_SKELETON = {
    "player_info" : {
        "total_xp" : 0,
        "level" : 1,
        "gold" : 0},

    "main_story" : {
        "act1" : "done",
        "act2" : "not_done",
        "act3" : "not_done", 
        "act4" : "not_done",
        "act5" : "not_done",
        "act6" : "not_done",
        "FINALE" : "not_done"
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
        "EASY GOLD OPPORTUNITY" : "not_done", # serlarp ofc

    },
    "forge" : {
        "status" : "empty", # can be empty, forging(??) or done
        "item" : None,
        "battles_until_done" : 0
    }
}


def save_game(save_data, file_loc):
    with open(file_loc, "w") as f:
        json.dump(save_data)

def load_game(save_data, file_loc): # this probably does NOT work right
    try:
        with open(file_loc, 'r') as f:
            load = json.load(f)
        current_format = SAVE_SKELETON.copy()
        current_format.update(load)
        return load
    except Exception:
        print("Error reading savefile.")
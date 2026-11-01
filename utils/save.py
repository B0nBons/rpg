import json
import os

# ok so ive never had to code in saving before so this is probably gonna be a hell of a ride
SAVE_SKELETON = {
    "player_info" : {
        "name" : "None", # so it erred on here when i ran so maybe none isnt allowed ??? changed it to text
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


def save_game(save_data, file_loc="data/save.json"):
    with open(file_loc, "w") as f:
        json.dump(save_data, f)
        # yeah so idfk how to make this work guys pls HELP

def load_game(file_loc="data/save.json"): # this probably does NOT work right
    try: # idk why i need save data actually, might jus be a chud
        with open(file_loc, 'r') as f:
            load = json.load(f)

        # trying to make it less hardcoded bc this will be a big problem latter 
        for thing in SAVE_SKELETON: # thing is the item in save eg forge
            if thing not in load: # if the item is not in the given save file
                load[thing] = SAVE_SKELETON[thing] # make the item the same as the generic 
                # so this may be a problem later (i genuinely forgot what i was thinking, but ik it will be a problem at some point.... so take that as you will lol)
        
        return load
    except Exception as e:
        print("Error reading savefile. " + str(e))
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
        "A Warrior's Guide To... Shopkeeping?" : "not_done"
    },
    "character_quests" : {
        "triton_act1" : "not_done", # might change this to be grouped by char, might not yeah i am def over organising ts, its  staying like this
        "perlos_act1" : "not_done", # will add more acts later, mostly just for testing purposes rn
        "duffaye_act1" : "not_done",
        "marchienne_act1" : "not_done",
        "serlapsia_act1" : "not_done", 

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

def load_game(save_data, file_loc):
    try:
        with open(file_loc, 'r') as f:
            load = json.load(f)
        current_format = SAVE_SKELETON.copy()
        current_format.update(load)
        return load
    except Exception:
        print("Error reading savefile.")
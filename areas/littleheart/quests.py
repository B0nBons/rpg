# QUEST BOARD TIME YESSS
# actually nevermind i have to make the village exist first
# first its gonna be a skeleton of the code since i really dont want to start the saves SAVE HAS BEEN MAYBE DONE
# ok in order to keep development moving at a decently-goodish pace, ive decided to use PLACEHOLDER variables that WILL be changed later to make better logic
# we survived!!!

# THEORETICAL IMPORTS (no longer theoretical)
from utils.save import load_game, save_game
from tabulate import tabulate
import time

MAIN_STORY_DEPENDENCIES = {
    "Mirexio, The Hated" : None,
    "Elysia, The Explorer" : "Mirexio, The Hated",
    "Twilia, The Lost" : "Elysia, The Explorer", 
    "Nemaro, The Seeker" : "Twilia, The Lost",
    "Klysari, The Queen" : "Nemaro, The Seeker",
    "Rumento, The Traitor" : "Klysari, The Queen",
    "Mirexio, The Storyteller" : "Rumento, The Traitor"
}

SIDE_QUEST_DEPENDENCIES = {
    # quest name : dependencies
    "A Warrior's Guide To... Shopkeeping?" : "act1"
}

CHAR_QUEST_DEPENDENCIES = {
    "perlos_act1" : None
}

# add more side quests later, now adding the actually important part of it (the CODE.)
# side note, but i finally found the library i used on my first big python project!!! we loev tabulate

def load_available_quests(save, mc):

    available_quests = []

    # yes, i am hardcoding it in, mostly since i dont foresee more than 3 types of quests existing
    for quest_name, status in save['main_story'].items():
        if status != "done":
            req = MAIN_STORY_DEPENDENCIES.get(quest_name)
            if req == None or save['main_story'].get(req) == "done":
                available_quests.append([quest_name, "Chasing Glory"])
        
    for quest_name, status in save['side_quests'].items():
        if status != "done":
            req = SIDE_QUEST_DEPENDENCIES.get(quest_name)
            if req == None or save['main_story'].get(req) == "done":
                available_quests.append([quest_name, "Adventure Requests"])

    for quest_name, status in save['character_quests'].items():
        if status != "done":
            if mc not in quest_name:
                req = CHAR_QUEST_DEPENDENCIES.get(quest_name)
                if req == None or save['main_story'].get(req) == "done":
                    available_quests.append([quest_name, "Local Help"])

    return available_quests

                # yeah im lazy and just copy pasted the first logic, but it should work right yay it worked, just pushed!

# NOTE: NAME THE FREAKING MAIN QUESTS SOMETHING OTHER THAN ACT1 AND ACT2

def quest_board(save=None, char=None):
    if save == None:
        save = load_game()
    if char == None:
        try:
            char = save['player_info']['name']
        except Exception as err:
            print("ERROR: Charactoer not Found")
    quests = load_available_quests(save, char)
    time.sleep(0.1)
    print(tabulate(quests, headers = ["Mission", "Focus"], tablefmt="fancy_grid"))
    hold = input("[END SO FAR]")

# the save file below is just for testing bc im lazy
SAVE_TEST_FILE = {
    # format of act : status (done/not_done)
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

    }
}

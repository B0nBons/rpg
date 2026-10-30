# QUEST BOARD TIME YESSS
# actually nevermind i have to make the village exist first
# first its gonna be a skeleton of the code since i really dont want to start the saves
# ok in order to keep development moving at a decently-goodish pace, ive decided to use PLACEHOLDER variables that WILL be changed later to make better logic
# also chat wish me luck (i have a bio test on friday and calc test on monday, lucky me... and ofc i agreed to go trick or treating with my friend so now I NEED to finish my hours asap)

# THEORETICAL IMPORTS
# from data.save import save
# from ???, import chosen_mc
from tabulate import tabulate

MAIN_STORY_DEPENDENCIES = {
    "act1" : None,
    "act2" : "act1",
    "act3" : "act2", 
    "act4" : "act3",
    "act5" : "act4",
    "act6" : "act5",
    "FINALE" : "act6"
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
                available_quests.append([quest_name, "Main Story"])
        
    for quest_name, status in save['side_quests'].items():
        if status != "done":
            req = SIDE_QUEST_DEPENDENCIES.get(quest_name)
            if req == None or save['main_story'].get(req) == "done":
                available_quests.append([quest_name, "SIde Story"])

    for quest_name, status in save['character_quests'].items():
        if status != "done":
            if mc not in quest_name:
                req = CHAR_QUEST_DEPENDENCIES.get(quest_name)
                if req == None or save['main_story'].get(req) == "done":
                    available_quests.append([quest_name, "Character Story"])

    return available_quests

                # yeah im lazy and just copy pasted the first logic, but it should work right yay it worked, just pushed!

# NOTE: NAME THE FREAKING MAIN QUESTS SOMETHING OTHER THAN ACT1 AND ACT2

def quest_board(save, char):
    quests = load_available_quests(save, char)
    print(tabulate(quests, headers = ["Mission", "Focus"], tablefmt="fancy_grid"))

save = {
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

# making a quick save skeleton to see if my logic works
# ok, so first for loop should return main story, then a SECOND for loop has to go inside the func, and print out the act/status? devlog here as benchmark
# ALRIGHT GUYS WE ARE DONE WITH THIS FILE (FOR NOW)
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

SIDE_QUESTS = {
    # quest name : dependencies
    "A Warrior's Guide To... Shopkeeping?" : "act1"
}

# add more side quests later, now adding the actually important part of it (the CODE.)
# side note, but i finally found the library i used on my first big python project!!! we loev tabulate

def load_available_quests(save, mc):
    for quest_type, story_log in save.items():
        for quest_NAME, status in story_log.items():
            print(f"Main location: {quest_type}, sub location {quest_NAME}, status {status}")
            if quest_NAME == mc:
                print("I HAVE FOUND THE MC QUEST OF " + quest_NAME)
                continue
def quest_board(char):
    pass

# making a quick save skeleton to see if my logic works
# ok, so first for loop should return main story, then a SECOND for loop has to go inside the func, and print out the act/status? devlog here as benchmark
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
        "a" : "done"
    },
    "character_quests" : {
        "triton_act1" : "done", # might change this to be grouped by char, might not yeah i am def over organising ts, its  staying like this
        "perlos_act1" : "done", # will add more acts later, mostly just for testing purposes rn
        "duffaye_act1" : "done",
        "marchienne_act1" : "done",
        "serlapsia_act1" : "done",

    }
}

chosen_mc = "triton"

load_available_quests(save, chosen_mc)
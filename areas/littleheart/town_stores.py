# OK TOWN STORE TIME
from utils.text_vfx import protag_talk as mc, typewriter as npc
from areas.littleheart.quests import quest_board
# i wish i could just make all print statements automatically use mc/npc talk based on context clues ts a pain in the ahh

# PLACEHOLDER SAVE STATE WILL BE USED

def forge(save):
    char = save['player_info']['name']
    # ok we are finally gonna start the shop code, w triton being the main mc nevermind im doing this next week bc its a massive update
    if mc == "triton":
        print("")
    else:
        npc(f"Triton: Hm? Hello {mc}. It's been a while since you've come here.")

def fishery(mc): 
    if mc == "perlos":
        print("yes this is perlos fishery where we eat fih")
    else:
        pass

def armory(mc):
    if mc == "marchienne":
        print("armory? more like ____ fun joke btw")
    else:
        pass

def farm(mc):
    if mc == "duffaye": # ok guys i dont know wtf duffate is gonna be doing bc he literally just owns a petting zoo OK I GOT IT HES GONNA BE A PETTING ZOO BUT BESTIARY THINGY
        print("dont mess with my homies (theyre all sheep)")
    else:
        pass

def general_store(mc):
    if mc == "serlapisa":
        print("why is she the only one who seems to logically be able to run a store")
    else:
        pass

def tavern(save):
    npc("Sirius: ...Who you are doesn't matter to me. Get to the quests.")
    npc("Sirius: How to accept quests? Well, just go ask the person for more details. I don't wanna post people's business everywhere.")
    quest_board(save)
    garbage = input("(... Well, I'm ready to get out now. [PRESS ENTER TO LEAVE])")
# now that everybodys stores have been defined im gonna go back and start implementing everything
# these comments are just helping me think out loud (talking to my laptop would make me seem insane)
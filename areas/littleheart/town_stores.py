# OK TOWN STORE TIME
from utils.text_vfx import protag_talk as mc, typewriter as npc
# i wish i could just make all print statements automatically use mc/npc talk based on context clues ts a pain in the ahh

# PLACEHOLDER SAVE STATE WILL BE USED

def forge(mc):
    # setup some things that need to be remembered for later
    # NEVERMIND WE NEED TO DO THE GAME STATE BRO
    # omg maybe i should make it so that whatever mc you choose owns a store to get some coins from it
    # im also trying to hit most my coding today and friday bc its halloween! 
    if mc == "triton":
        print("yeah this is my store fr")
        # im not making tritons shop yet guys
    else:
        npc(f"Triton: Hm? Hello {mc}. It's been a while since you've come here.")
        

def fishery(mc): 
    if mc == "perlos":
        print("yes this is perlos fishery where we eat fih")

def armory(mc):
    if mc == "marchienne":
        print("armory? more like ____ fun joke btw")

def farm(mc):
    if mc == "duffaye": # ok guys i dont know wtf duffate is gonna be doing bc he literally just owns a petting zoo OK I GOT IT HES GONNA BE A PETTING ZOO BUT BESTIARY THINGY
        print("dont mess with my homies (theyre all sheep)")

def general_store(mc):
    if mc == "serlapisa":
        print("why is she the only one who seems to logically be able to run a store")
# now that everybodys stores have been defined im gonna go back and start implementing everything
# these comments are just helping me think out loud (talking to my laptop would make me seem insane)
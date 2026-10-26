# ok were so back, we gonna make some very EASY enemies first, then go on as weeks progress. i hope somebody enjoys this rpg and actually plays it since this is gonna take a TON of work (whym i such a chud shouldve just gone for unreal engine vro
# bringing the best char perlos in to see how i structured her and named stuff
# SHIT I NEED A MAGICAL DEFENSE SECTION, ok this is fixed but im gonna keep my comments until week 12 bc i bet some of them are gon be really funny when i look back on them
# the current system for xp is gonna be half the vitality
import random
import copy

EASY_CHUDS_FOREST = [
    {"name" : "Apologetic Toadstool" , "vi" : 12, "ap" : 1, "dp" : 0, "magic_res" : 1, "xp" : 4, 
     "loot" : {
         "MUSHROOM" : 0.3 # its a dict bc i might add more loot idk
     }},
    {"name" : "Aggrivated Wisp", "vi" : 16, "ap" : 6, "dp" : 2, "magic_res" : 2, "xp" : 6,
     "loot" : {
          "GHOST IN A BOTTLE" : 0.2
     } },
    {"name" : "Not-Stationary Tree", "vi" : 20, "ap" : 5, "dp" : 1, "magic_res" : 0, "xp" : 6,
     "loot" : {
          "WOOD" : 0.3,
          "STONE" : 0.5 # bc the trees throw rocks at u ig
     }},
    {"name" : "Mossy Toad", "vi" : 8, "ap" : 5, "dp" : 0, "magic_res" : 0, "xp" : 4,
     "loot" : {
          "MOSS" : 0.8,
          "BERRIES" : 0.5
     }}
]

HARD_BOSS_FOREST = [
    {"name": "Mold-Soaked Crocodile", "vi" : 30, "ap" : 8, "dp" : 2, "magic_res" : 1, "xp" : 16,
     "loot" : {
         "CROCODILE SCALE" : .1
     }} #rouund up to even, prolly change xp later
]

def grab_forest(boss=False):
    if boss:
        return copy.deepcopy(HARD_BOSS_FOREST)
    # i thought that maybe the hp/vi bug was because of it pointing to the same memory address, but it doesnt seem to be that so i honestly have NO idea how to fix that.... lol.
    
    num_enemies = random.randint(1,5)
    return (copy.deepcopy(random.choices(EASY_CHUDS_FOREST, k=num_enemies)))
# we need deepcopy bc otherwise hp changes will affect the main/bestiary hp (no clue if im using bestiary right)
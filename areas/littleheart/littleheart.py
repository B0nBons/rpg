# ok this is the main village file
# i think i might just use an image to ascii converter for now since as i said, my ascii art is more like AHHscii art (HILARIOUS)
from areas.littleheart.town_stores import tavern
import time

def village(save):
    print("This village appears to be nothing more than dust and bones...")
    print("Yet, it holds all the memories you know.")
    print("VI restored to max.")
    print("MP restored to max.")
    time.sleep(0.1)
    # only for now to introduce quests and stuff
    print("Despite having lived here forever, you never thought the day would ever come. Becoming a licensed guardian was no small feat...")
    print("Alas, you had to go to the tavern to get licensed...")
    print("You decide to go to the other stores after going to the tavern.")
    time.sleep(0.2)
    tavern(save)

def update(save):
    pass
    # this village is meant to be the fully integrated version, with the top version only being a temp hold one


# yeah so first i need to make the stores, quests, and npc chatter first..........
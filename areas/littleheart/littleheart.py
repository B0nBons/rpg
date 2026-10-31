# ok this is the main village file
# i think i might just use an image to ascii converter for now since as i said, my ascii art is more like AHHscii art (HILARIOUS)
from areas.littleheart.town_stores import tavern
import time

def village():
    print("This village appears to be nothing more than dust and bones...")
    print("Yet, it holds all the memories you know.")
    print("VI restored to max.")
    print("MP restored to max.")
    time.sleep(0.1)
    print("...")
    print("You have a strong feeling that you need to go to the tavern.")
    tavern()


# yeah so first i need to make the stores, quests, and npc chatter first..........
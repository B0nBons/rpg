import json
import os

# ok so ive never had to code in saving before so this is probably gonna be a hell of a ride
SAVE_SKELETON = {
    "player_info" : {
        "total_xp" : 0,
        "level" : 1,
        "gold" : 0
    },
    "main_story_progress" : {
        "PLACEHOLDER" : "done" # done=done, unstarted=unstarted, and i think itll just be that and maybe have no main story checkpoints (you need to sit  down and do all of it)
    },
    "forge" : {
        "status" : "empty", # can be empty, forging(??) or done
        "item" : None,
        "battles_until_done" : 0
    }
}

def save_game():
    pass

def  load_game():
    pass
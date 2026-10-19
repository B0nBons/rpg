# rpg game inspired by candybox(1/2) and a dark room (peak)
import time
from pick import pick
import colorama

colorama.init(autoreset=True)

characters = [
    {
    "name" : "Larperino Triton",
    "age" : 26,
    "job" : "Blacksmith",   # make jobs into classes?
    "ap" : 8, # attack power
    "dp" : 11, # defense points (FLAT WITH NO PAASSIVE)
    "spe" : 6, # speed (for turn order)
    "vi" : 30, # vitality
    "potions" : 3, # num of potions that can be carried
    "magic" : 4, # low magic aptitude
    "magic-style" : "FIRE", #higher the magic stat, more  magic dmg and chance for magic effects
    "style" : "Low speed, great attack and defense. Has an unrealized natural aptitude for FIRE magic.",
    "passive" : "Has a 20 percent chance of deflecting attacks. Gain +2DP when in combat for more than 3 turns, and +6DP when in combat for more than 6." #power scaling gonna be so 
    },
# next char
    {
    "name" : "Marienna Perlos",
    "age" : 23,
    "job" : "Fisherman",
    "ap" : 6,
    "dp" : 7, #not 67 funny
    "spe" : 12,
    "vi" : 20,
    "potions" : 3,
    "magic" : 6,
    "magic-style" : "WATER", #duh
    "style" : "High speed, and all-rounded stats. Despite this, she swears that she doesn't use WATER magic to catch her fish...",
    "passive" : "Has a 20 percent chance of launching an additional attack after her turn. For every three attacks, add an additional attack."
    },
# next char (this is gonna be so powercreep) just realised i forgot health bro what am i doing
    {
    "name" : "Oasias Marchienne",
    "age" : 26,
    "job" : "Hunter",
    "ap" : 10,
    "dp" : 4,
    "spe" : 15,
    "vi" : 20,
    "potions" : 4,
    "magic" : 2,
    "magic-style" : "BLOOD",
    "style" : "They are fastest in the village, with high attack power and low magic affinity. Perhaps something could be done about that? Despite Duffaye's attempts, she still manages to smuggle fresh meat past him.",
    "passive" : "When hit in battle, gain +1AP. If more than 4VI was lost in one hit, additionally gain +1DP." 
    },
# next char, lowkey i do like where this is going
    {
    "name" : "Geomoros Duffaye",
    "age" : 22, # an old soul ahh
    "job" : "Farmer",
    "ap" : 4,
    "dp" : 2,
    "spe" : 8,
    "vi" : 20,
    "potions" : 5,
    "magic" : 5,
    "magic-style" : "ANIMAL",
    "style" : "Despite being one of the youngest farmers in the village, he can take more than anyone else. He has a love for ANIMALS, and encouraged the entire village to turn pescatarian. What a guy...",
    "passive" : "When hit in battle, gain +1MAGIC. Every five turns, remove all MAGIC, and have one random animal join the battle (MAX 2 TOTAL)."
    },
# bro what in the infinite summons is ts gonna be, he is being IGNORED until i figure out how the FAH he would work
    {
    "name" : "Eleosa Serlapisa",
    "age" : 25,
    "job" : "Merchant",
    "ap" : 7,
    "dp" : 7,
    "spe" : 7,
    "vi" : 30,
    "potions" : 3,
    "magic" : 7,
    "magic-style" : "WIND",
    "style" : "She never seems to have customers, yet always has gold. People who go to her for help and advice... Never quite come back the same.",
    "passive" : "For every enemy in battle, gain +2AP and +2DP. Every turn, roll a dice and give allies a random buff, scaling off MAGIC."
    }
]

# I AM NOT DOING MORE CHARACTERS THAT TOOK SO FREAKING LONG IMA CRASHOUT

intro_play_ONCE =  "placehold"
# weekly theme is outdoors so maybe start with the more adventure-y parts

def typewriter(text, speed_s = 0.04):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(speed_s)
    print("\n")
    return text
    # thank you stack overflow


# we give mc BRIGHT text to differentiate who is talking, npc might get grey or som
def protag_talk(text):
    for letter in text:
        print(colorama.Style.BRIGHT + letter, end='', flush=True)
        time.sleep(0.05)
    print("\n")
    return text

def main():
    typewriter("Well, aren't you a sight for sore eyes!\nIt's been such a long time since I've seen you!\n...\nI still remember when you fell off a tree when you were young!\nWell then, youngster! What do you call yourself now?\n")

    char_choice = protag_talk("...What is my name again?")
    char_list = ['Triton (he/him/his)', 'Perlos (she/her/hers)', 'Marchienne (they/them/theirs)', 'Duffaye (he/him/his)', 'Serlapisa (she/her/hers)']
    char = pick(char_list, char_choice)

    if char[1] == 0:
        char = "Triton"
        protag_talk(f"{char}: My name? It's {char}. I uh. I haven't changed it at all..")
        typewriter(f"Granny Duffaye: Oh relax {char}! Remember when you used to call yourself ""Mister Rock Eater-""")
        protag_talk(f"{char}: Okay, okay, what did you need? I'll do it, just don't bring that up again..")
        typewriter("Granny Duffaye: As straight to the point as ever! I was told you need to go see Mirexio. I'm not sure of what the old hag wants from you, but she insisted it was urgent..")
        protag_talk(f"{char}: ... Urgent? Then I ought to go right away. Thank you for informing me.")
        typewriter("Granny Duffaye: (As formal as ever... Oh, when will you learn to relax, Triton?)")

    elif char[1] == 1:
        char = "Perlos"
        protag_talk(f"{char}: Oh come on, Miss Duffaye! It's me, {char}!")
        typewriter(f"Granny Duffaye: Ah, I know, I know, {char}! No need to get all fired up on me! I have a message for you.. It's from Mirexio.")
        protag_talk(f"{char}: Mirexio..? I thought she was-")
        typewriter("Granny Duffaye: Kicked out? Yep. Nobody wanted that necromancy in our village. She told me it was urgent.")
        protag_talk(f"{char}: Thank you, Miss Duffaye! I can go see her now. What a shame... I almost beat my fishing record today...")
        typewriter("Granny Duffaye: (That child, with her head in the clouds... It's a miracle she's even lived this long!)")

    elif char[1] == 2:
        char = "Marchienne"
        protag_talk(f"Oasias Marchienne.")
        typewriter("Granny Duffaye: ...Ah. I ought to not have bothered you, miss Oasias. I can come at a later time-")
        protag_talk(f"{char}: No. Please tell me. If this is urgent, I must be the first to know.")
        typewriter("Granny Duffaye: ...I was told you need to go see Mirexio. She said it was urgent..")
        protag_talk(f"{char}: Thank you for informing me. I shall go pay her a visit.")
        typewriter("Granny Duffaye: (...Even after she's left, I still can feel my heart pounding. I see why all the others fear her...)")

    elif char[1] == 3:
        char = "Duffaye"
        protag_talk(f"{char}: Grandma! This isn't the time to be telling jokes!")
        typewriter("Granny Duffaye: Hahaha, of course I know who you are, Geomoros! Can't a grandmother ask her favorite boy a silly question?!")
        protag_talk(f"{char}: Hmph. Not funny grandma! You scared me there for a- hey, what's that letter? Is that from-")
        typewriter("Granny Duffaye: ...Yes, my dear boy. Mirexio. She told me that you ought to go visit her, as soon as possible.")
        protag_talk(f"{char}: Well then, of course I'm gonna go! Her home is a bit far out, so I'll start packing. Thanks gran!")
        typewriter("Granny Duffaye: (How he manages to see the good in everyone, and only the good... Is truly a question that not even I can answer.)")
    else:
        char = "Serlapisa" 
        protag_talk(f"{char}: Oh c'mon, you don't remember me? I'm Serlapisa. I used to tell your grandson I'd steal all his sheep and sell their wool. Remember?")
        typewriter("Granny Duffaye: Serlapisa, that was you?! He was so upset after you said that, he refused to leave his sheep for a week!")
        protag_talk(f"{char}: ...Oops. I thought he told you.")
        typewriter("Granny Duffaye: We can discuss this later. I was told by Mirexio that you need to go see her. She told me it was urgent.")
        protag_talk(f"{char}: Mirexio? Wasn't she that witch who got kicked out? Hehehe, I bet she could make me an infinite money potion! I'll get going, thanks granny!")
        typewriter("Granny Duffaye: (She was the one who was tormenting Geomoros?! He told me his tormenter had been eaten by wolves!)")
    

main()

#dawg ima crashout
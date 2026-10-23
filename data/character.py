# hey guys i wrote the battle system and ngl i think i made everybodys stats too good 
# so consider this october 22/2026 as the first ever NERF to everybody!

triton = {
    "name" : "Larperino Triton",
    "age" : 26,
    "job" : "Blacksmith",   # make jobs into classes?
    "ap" : 8, # attack power
    "dp" : 5, # defense points (FLAT WITH NO PAASSIVE)
    "spe" : 6, # speed (for turn order)
    "vi" : 30, # vitality
    "potions" : 3, # num of potions that can be carried
    "magic" : 4, # low magic aptitude
    "magic_res" : 8,
    "magic_style" : "FIRE", #higher the magic stat, more  magic dmg and chance for magic effects
    "style" : "Low speed, great attack and defense. Has an unrealized natural aptitude for FIRE magic.",
    "passive" : "Has a 20 percent chance of deflecting attacks. Gain +2DP when in combat for more than 3 turns, and +6DP when in combat for more than 6." #power scaling gonna be so 
    }

perlos = {
    "name" : "Marienna Perlos",
    "age" : 23,
    "job" : "Fisherman",
    "ap" : 6,
    "dp" : 4, #not 67 funny
    "spe" : 12,
    "vi" : 20,
    "potions" : 3,
    "magic" : 6,
    "magic_res" : 3,
    "magic_style" : "WATER", #duh
    "style" : "High speed, and all-rounded stats. Despite this, she swears that she doesn't use WATER magic to catch her fish...",
    "passive" : "Has a 20 percent chance of launching an additional attack after her turn. For every three attacks, add an additional attack."
    }

marchienne = {
    "name" : "Oasias Marchienne",
    "age" : 26,
    "job" : "Hunter",
    "ap" : 10,
    "dp" : 4,
    "spe" : 15,
    "vi" : 20,
    "potions" : 4,
    "magic" : 2,
    "magic_res" : 6,
    "magic_style" : "BLOOD",
    "style" : "They are fastest in the village, with high attack power and low magic affinity. Perhaps something could be done about that? Despite Duffaye's attempts, she still manages to smuggle fresh meat past him.",
    "passive" : "When hit in battle, gain +1AP. If more than 4VI was lost in one hit, additionally gain +1DP." 
    }

duffaye = {
    "name" : "Geomoros Duffaye",
    "age" : 22, # an old soul ahh
    "job" : "Farmer",
    "ap" : 5,
    "dp" : 4,
    "spe" : 8,
    "vi" : 30,
    "potions" : 2,
    "magic" : 8,
    "magic_res" : 2, #since he has a fairly high aptitude for magic, hes worse at blocking it out
    "magic_style" : "ANIMAL",
    "style" : "Despite being one of the youngest farmers in the village, he can take more than anyone else. He has a love for ANIMALS, and encouraged the entire village to turn pescatarian. What a guy...",
    "passive" : "When hit in battle, gain +1MAGIC. Every five turns, remove all MAGIC, and have one random animal join the battle (MAX 2 TOTAL)."
    }

serlapisa = {
    "name" : "Eleosa Serlapisa",
    "age" : 25,
    "job" : "Merchant",
    "ap" : 7,
    "dp" : 7,
    "spe" : 7,
    "vi" : 30,
    "potions" : 3,
    "magic" : 7,
    "magic_res" : 2, # itd be funny if she was like third wall breaking or som
    "magic_style" : "WIND",
    "style" : "She never seems to have customers, yet always has gold. People who go to her for help and advice... Never quite come back the same.",
    "passive" : "For every enemy in battle, gain +2AP and +2DP. Every turn, roll a dice and give allies a random buff, scaling off MAGIC."
    }
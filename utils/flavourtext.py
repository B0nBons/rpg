import random
# YASSSS WE DOIN FLAVOURTEXT >:)
# gonna make a small key of the main areas

AREAS = ["Littleheart Village", "Lonely Forest", "The Cabin of Miss Mirexio" ,"Echoing Caves", "Frozen Wastes", "Tearfull Waterways", "Haeropheus City", "Laceleaf Depths"]
AREAS_FUN = {"Home", "Peaceful Trees", "Mirexio's House",    "Can't-Shut-Up Caverns", "Trashdump", "Levenia's Best Water Park!", "Toasty-Warm Home", "Butterfly Ravines"} # four left ahh
AREAS_SERIOUS = {"Their Home", "Forest", "Abandoned Home", "Caves", "Wastes", "Waterways", "Their City", "Ravines"}
# maybe based on options, they get locked into a normal, fun, or serious route, in which case,
# areas = what the characters' adventure was like
# areas_fun = what the characters said the adventure was like
# areas_serious = what really happened (to be unlocked in the last POV, not pushing bc spoilers)

FOREST = {
    "Apologetic Toadstool" : {
        "triton" : ["...A mushroom?", "Is this what my life has come to?", "I usually eat my mushrooms.."],
        "perlos" : ["Eh? I hate mushrooms! Get away from me!!!", "Everyone knows fish tastes much better than-than this!", "Ew. Ew. Ew.. Can we please just, not fight?"],
        "marchienne" : ["...", "Stay out of my way.", "... There isn't mush-room for the both of us."],
        "duffaye" : ["Cmon, we can be friends!", "We don't need to fight...", "Nature really is extraordinary.."],
        "selapisa" : ["I'm sure I could get a coin or two for you!", "Just come along quietly..", "Ahh, I can just imagine the mushroom soup!"]
                             },
    "Aggrivated Wisp" : {
        "triton" : ["Ghosts aren't real..", "It's glowing... Like a light to guide the way.", "A life well lived, but now, it is time to rest.."],
        "perlos" : ["Waahhh?! A ghost?!", "This isn't the souls of all those fish coming to haunt me... R-right?", "It's so toasty... Maybe I can cook some fish on it!"],
        "marchienna" : ["...", "I have no reason to fight with the dead.", "This is quite wisp-y business. Not. Get out of my way."],
        "duffaye" : ["I uh, don't usually see wisps...", "I've been nothing but peaceful, and yet you want to fight me?!", "Why couldn't I be finding anything else... Like a tree?!"],
        "selapisa" : ["A wisp?! Care to lead me to great treasures?", "Even the dead are stingy...", "Just come with me! Heheh, you'll be worth a fortune.."]
    }, 
    "Not-Stationary Tree" : {
        "triton" : ["Surely the world is playing a cruel joke on me...", "I will bring you a swift end.", "Talk about a walking fire hazard..."],
        "perlos" : ["Whoa, maybe you can help me catch fish!", "Aww, it's kinda cute! I wanna keep it!", "Those branches... so sharp..."],
        "marchienne" : ["...", "A waste of wood.", "Put those roots down, and stop moving!"],
        "duffaye" : ["I can find anything in this forest. Escept for a peaceful animal.", "Just stop chasing me!", "I wonder.. Those branches are so sharp. Must make climbing easy.."],
        "selapisa" : ["Those branches... I could sell them to any unskilled sorcerer-", "Just follow me, and I'll make sure everyone knows what you're worth...", "The foilage... It's perfect!"]
    },
    "Mossy Toad" : {
        "triton" : ["(This thing is more moss than toad...)", "Just move.", "It looks like a corpse being controlled by a parasite..."],
        "perlos" : ["Why have plants and animals, when you can just combine them!", "Awww, c'mere Mossball!", "I'll hit you all the way to the stars!"],
        "Marchienne" : ["...", "Disgusting. A parasitic abomination of nature.", "You aren't growing on me."],
        "duffaye" : ["No animal deserves this...", "At least it lived a nice life.", "I'll bury you after this.. You never deserved this, froggy.."],
        "selapisa" : ["Moss paarasites are especially rare now...", "I'm sure a collector would pay a fortune for you!", "More moss than toad. A sad way to live."]
    },
    "Mold-Soaked Crocodile" : {
        "triton" : ["Finally, a real challenge.", "Perlos would want this..", "I'll remove the rot, so deep in your soul."],
        "perlos" : ["Huh... So this is where you went, Croco.", "It'll be for the best..", "Everything will be better. I promise."],
        "marchienne" : ["...", "Perlos did say that crocodile that sat with her left one day, and never came back.", "You will be a crocodeadle when I'm done with you."],
        "duffaye" : ["Oh come on.. I don't wanna tell Perlos...", "It's all for the greater good..", "I won't let you hurt any longer."],
        "selapisa" : {"Haha, a skin like that would be worth a fortune!", "Perlos... Wouldn't want to know.", "I'll put you out of your misery."}
    }
}

#triton
#perlos
#marchienne
#duffaye
#selapisa
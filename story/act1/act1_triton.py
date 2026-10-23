from utils.text_vfx import typewriter as npc, protag_talk as mc, narrator as narr
from utils.battle import forest_fight
# to test story files run cd /workspaces/rpg && python3 -m story.act1.act1_triton
# maybe make an action writer for more pop
def triton_act1():
    print("\n\n\n\n\n")
# now that battles work, I wanted to rewrite tritons first act, since it felt to me like he very much fell flat as a character, and wasnt interesting
    mc("Triton: ...Sigh. Mirexio just had to get banished all the way past the forest..")
    mc("Triton: (It wasn't her choice though. I ought to not judge her for something out of her control.)")
    narr("The lively chatter of Littleheart Village fades away. It is silent, except for the faint croaking of frogs, and rustling of plants.")
    mc("Triton: (...It's too quiet. What in the world could've happened?)")
    narr("Triton cautiously reaches towards the sword on his back... And all of a sudden-")
    battleA = forest_fight("triton")
    # after doing some testing - it works, there DOES seem to be a tiny bug on considering enemies dead (saw a toadstool at -2 hp)
    if not battleA:
        narr("Later that day, Littleheart village would lose Triton to the beasts of the forest.")
        narr("Some say he became yet another wisp, and was finally reunited with his family.")
        return False
    mc("Triton: What a waste of time. At this rate, I'll be lucky to get to Mirexio's by dusk.")
    

triton_act1()
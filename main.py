# rpg game inspired by candybox(1/2) and a dark room (peak)
import time
from pick import pick
import colorama
from utils.text_vfx import typewriter, protag_talk
from utils.battle import forest_fight
colorama.init(autoreset=True)

intro_play_ONCE =  "placehold"
# weekly theme is outdoors so maybe start with the more adventure-y parts

def main():
    global char
    typewriter("Another quiet day in the home you know as Littleheart Village. As you walk past the once-lively town square, you can't help but think about the past. So much has changed in the past year. It feels almost surreal. You look at your reflection in the puddle. Who was that, staring back at you?")

    char_choice = protag_talk("...What is my name again?")
    garbage = input("(Before making options, you will have the chance to review previous dialouge and press ENTER in order to continue to your choice. Think carefully, for each choice may cause you to take an unexpected path)...\nPlease press ENTER.")
    char_list = ['Triton (he/him/his)', 'Perlos (she/her/hers)', 'Marchienne (they/them/theirs (NOTE: They do use "miss" as of now, I hope thats not a major issue for now))', 'Duffaye (he/him/his)', 'Serlapisa (she/her/hers)']
    char = pick(char_list, char_choice)

    typewriter("Just then, an overly-excited voice pulls you from your thoughts.\n???: Hey, you there! What's your name? Tell me the right name, and I'll give you your mail!")

    if char[1] == 0:
        char = "Triton"
        protag_talk(f"{char}: My name? It's {char}. Did you need something... Miss Duffaye..?")
        typewriter(f"Granny Duffaye: Oh relax {char}! Remember when you used to call yourself ""Mister Rock Eater-""")
        protag_talk(f"{char}: Okay, okay, what did you need? I'll do it, just don't bring that up again..")
        typewriter("Granny Duffaye: As straight to the point as ever! I was told you need to go see Mirexio. I'm not sure of what the old hag wants from you, but she insisted it was urgent..")
        protag_talk(f"{char}: ... Urgent? Then I ought to go right away. Thank you for informing me.")
        typewriter("Granny Duffaye: (As formal as ever... Oh, when will you learn to relax, Triton?)")
        forest_fight("triton")

    elif char[1] == 1:
        char = "Perlos"
        protag_talk(f"{char}: Oh come on, Miss Duffaye! It's me, {char}!")
        typewriter(f"Granny Duffaye: Ah, I know, I know, {char}! No need to get all fired up on me! I have a message for you.. It's from Mirexio.")
        protag_talk(f"{char}: Mirexio..? I thought she was-")
        typewriter("Granny Duffaye: Kicked out? Yep. Nobody wanted that necromancy in our village. She told me it was urgent.")
        protag_talk(f"{char}: Thank you, Miss Duffaye! I can go see her now. What a shame... I almost beat my fishing record today...")
        typewriter("Granny Duffaye: (That child, with her head in the clouds... It's a miracle she's even lived this long!)")
        forest_fight("perlos")

    elif char[1] == 2:
        char = "Marchienne"
        protag_talk(f"Oasias Marchienne.")
        typewriter("Granny Duffaye: ...Ah. I ought to not have bothered you, miss Oasias. I can come at a later time-")
        protag_talk(f"{char}: No. Please tell me. If this is urgent, I must be the first to know.")
        typewriter("Granny Duffaye: ...I was told you need to go see Mirexio. She said it was urgent..")
        protag_talk(f"{char}: Thank you for informing me. I shall go pay her a visit.")
        typewriter("Granny Duffaye: (...Even after she's left, I still can feel my heart pounding. I see why all the others fear her...)")
        forest_fight("marchienne")

    elif char[1] == 3:
        char = "Duffaye"
        protag_talk(f"{char}: Grandma! This isn't the time to be telling jokes!")
        typewriter("Granny Duffaye: Hahaha, of course I know who you are, Geomoros! Can't a grandmother ask her favorite boy a silly question?!")
        protag_talk(f"{char}: Hmph. Not funny grandma! You scared me there for a- hey, what's that letter? Is that from-")
        typewriter("Granny Duffaye: ...Yes, my dear boy. Mirexio. She told me that you ought to go visit her, as soon as possible.")
        protag_talk(f"{char}: Well then, of course I'm gonna go! Her home is a bit far out, so I'll start packing. Thanks gran!")
        typewriter("Granny Duffaye: (How he manages to see the good in everyone, and only the good... Is truly a question that not even I can answer.)")
        forest_fight("duffaye")
    else:
        char = "Serlapisa" 
        protag_talk(f"{char}: Oh c'mon, you don't remember me? I'm Serlapisa. I used to tell your grandson I'd steal all his sheep and sell their wool. Remember?")
        typewriter("Granny Duffaye: Serlapisa, that was you?! He was so upset after you said that, he refused to leave his sheep for a week!")
        protag_talk(f"{char}: ...Oops. I thought he told you.")
        typewriter("Granny Duffaye: We can discuss this later. I was told by Mirexio that you need to go see her. She told me it was urgent.")
        protag_talk(f"{char}: Mirexio? Wasn't she that witch who got kicked out? Hehehe, I bet she could make me an infinite money potion! I'll get going, thanks granny!")
        typewriter("Granny Duffaye: (She was the one who was tormenting Geomoros?! He told me his tormenter had been eaten by wolves!)")
        forest_fight("serlapisa")

    time.sleep(1)
    protag_talk(f"{char}: (I wonder what Mirexio could possibly want. She knows that after what she did, she isn't welcomed by most anyone... But if she says it's urgent, then I believe her. She wouldn't call something urgent if it wasn't.)")
    print(".. -. / - .... . / . -. -.. --..-- / .-- . / .- .-.. .-.. / .-.. .. . -..")
    #typewriter("""
#▀█▀ █░█ █▀▀   █░░ █ ▄▀█ █▀█   █░█░█ ▄▀█ █▀   █▀▄▀█ █▀▀
#░█░ █▀█ ██▄   █▄▄ █ █▀█ █▀▄   ▀▄▀▄▀ █▀█ ▄█   █░▀░█ ██▄""", 0.08)

    typewriter("A (SOON TO BE) VISUAL NOVEL")
    print("-... ..- - / .. - / .-- .- ... / -. . ...- . .-. / - .... . .. .-. / ..-. .- ..- .-.. -")

    # yeah so we are not in fact doing a linear act thing, were making it (kinda) open world

    while True:
        pass

if __name__ == "__main__":
    main()
# ALRIGHT WE MAKING A BATTLE SYSTEM W THIS ONE
# ts gonna be hard isnt it
import random
import time
from pick import pick
import colorama
from data.enemies import grab_forest
from utils.flavourtext import FOREST 
from data.character import triton, perlos, marchienne, duffaye, serlapisa
from utils.text_vfx import protag_talk as mc
# ok i need to go back and review all of the names bc serlapisa is called selapisa???
colorama.init(autoreset=True)

chars = {"triton" : triton, "perlos" : perlos, "marchienne" : marchienne, "duffaye" : duffaye, "selapisa" : serlapisa}
# i think ive been spelling their names wrong.......

def checK_mc():
    pass

def grab_MC_talk(enemy_name, mc):
    if enemy_name in FOREST:
        lines = FOREST[enemy_name] # review dicts bc i do not remember this at all

def forest_fight(char = marchienne, boss=False):
    if char not in chars:
        print("yo this means the char is invalid")
        return NameError

    player = chars[char].copy() # copy bc we dont want to mess with our # og list :)
    player['current_vi'] = player['vi']
    player['temp_ap'] = player['ap']
    player['temp_dp'] = player['dp']

    enemies = grab_forest(boss=boss) # goofiest ahhs formatting ive seen 
    print(colorama.Fore.RED + colorama.Style.BRIGHT + "\n(cool text thing) COMBAT CONFIRMED (cool text thing but right side)\n")

    for enemy in enemies:
        flavourtext = FOREST[enemy['name']][char]
        spoken = random.choice(flavourtext)
        mc(f"{char.capitalize()} encountered {enemy['name']}!!!")
        mc(f"{char.capitalize()}: {spoken}")

    turn_count = 0 # define before loop to avoid error

    while player["current_vi"] > 0 and len(enemies) > 0:
        turn_count += 1
        print(colorama.Fore.YELLOW + f"(cool text effect) {turn_count} (cool text effect)")
        print(f"{player['name']} HP: {player['current_vi']}/{player['vi']} POTIONS: {player['potions']}")

        # we add the turn passives (literally jus triton fn)

        if char == "Triton":
            if turn_count == 4:
                player['temp_dp'] += 2
                print("Triton gains +2DP (PASSIVE)")
            elif turn_count == 7:
                player['temp_dp'] += 4
                print("Triton gains +4DP (PASSIVE)") # change scaling, he might be too good early game

        trash = input("Press ENTER when ready to make a choice...")
        choices = ["ATTACK", "CAST SPELL", "USE POTION", "FLEE"]
        title = f"What will {char} do?"
        choice, trash = pick(choices, title)

        if choice == "ATTACK" : 
            enemy_name = []
            for pain in enemies:
                enemy_vi = f"{pain['name']} HP: {pain['vi']}"
                enemy_name.append(enemy_vi) #shouldve just made it hp, vi is NOT quirky and fun 
            garbage, TARGET_IND = pick(enemy_name, "Select Target:")
            target = enemies[TARGET_IND]

            # now we get to dmg calcs

            damage = player['temp_ap'] - target['dp']
            target['vi'] -= damage
            mc(f"{char.capitalize()} hit {target['name']} for {damage}!") # ___ damage?? ___ VI??? wtf do i put its so naked

            # uhh now we look if its dead lol

            if target['vi'] <= 0:
                mc(f"Yay! {char.capitalize()} killed {target['name']}!!!")
                enemies.pop(TARGET_IND) # why dont people just use capital variables? so much easier to read lowkey

            if char == "perlos":
                followup_chance = random.randint(0,100)
                if followup_chance <= 70: # IT IS NOT MEANT TO BE 70 OR MORE THIS IS FOR TESTING IF THIS IS STILL HERE BY LIKE WEEK FOUR PLEASE TELL ME TO DELETE THIS BECAUSE PERLOS IS NOT MEANT TO BE A SPEEDRUNNER
                    if len(enemies) > 0:
                        victim = random.choice(enemies) 
                        dmg = player['temp_ap'] - target['dp']
                        victim['vi'] -= dmg
                        mc(f"Perlose throws a fishing line at {victim['name']}! The unkindness of this deals an additional {dmg} damage!")
                        if victim['vi'] <= 0:
                            mc(f"Perlos fishes up another for her collection! {victim['name']} was defeated!")
                            enemies.remove(victim)

            elif choice == "CAST SPELL":
                mc("!!! A magical power seems to be awakening....")
                print("my bad gang i havent done this yet, also nobody gets magic until chapter 2 or 3, so hold your horses")
                mc("You get the feeling that being patient will make your life a lot better. You decide to let the ENEMIES attack first.")

            elif choice == "FLEE":
                if boss == True:
                    mc(f"{char} : I'm not going to run away.")
                elif boss == False:
                    chance = random.randint(0,100)
                    if chance <= 25:
                        print("COWARD OVER HERE!!! You fled the battle. No XP gained.")
                        return False # loser lol

            # now we check if enemies died

            if len(enemies) == 0:
                mc("BATTLE DECIDED... You win!")
                return True # YAY

            # yeah thats the win idk man
            # now we have to do enemies (because undertale genocoide sim is not tuff)

            print("ENEMY TURN (COOL TEXT THING ON BOTH SIDES)")
            for enemy in enemies:
                if char == "triton":
                    deflect_chance = random.randint(0,100)
                    if deflect_chance <= 20: # CHANGE THIS ITS FOR TESTING ok it works i think
                        mc(f"Triton steadies his blade, and DEFLECTS {enemy['name']}'s attack!")
                        time.sleep(0.2)
                        continue # yooo rare continue reference guys

                enemy_damage = enemy['ap'] - player['temp_dp']
                player['current_vi'] -= enemy_damage
                mc(f"Owch! {char.capitalize()} got hit by {enemy['name']} for {enemy_damage} damage!")
                garbage = input("Press ENTER to continue...")

                # now we do marchienne passive of free attack
                if char == "marchienne":
                    player['temp_ap'] += 1
                    mc(f"{char}: I won't let you do that again.")
                    print(f"{char.capitalize()} gained +1 AP")
                    if enemy_damage >= 4:
                        player['temp_dp'] += 1
                        mc(f"{char}: I'll make you pay.")
                        print("Marchienne gains an additional 1 AP...")

                if player['current_vi'] <= 0:
                    print("YOU LOST, TRY NOT SUCKING")
                    return False


            # SHIT I FORGOT TO MAKE SPEED RELEVANT. ok i think itll just be irrelevant for now until i maybe make it into an actual visual novel ahh game

forest_fight("marchienne")
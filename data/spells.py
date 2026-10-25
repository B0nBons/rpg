# were finally getting into the MAGIC w this one!!!!!
# I think were gonna seperate them by type (since i think im just doing 1mc per spell type)
# then itll be formatted with name,magic cost,buff/debuff, and a lil info blurb bc i love writing blurbs
# side note but why is my cursor not lining up with my typing wtf is codespaces even doin atp

spells = {
    "FIRE" : {
        "THERMAL" :{
            "name" : "Thermal Sink",
            "style" : "Fire",
            "cost" : 3,
            "power" : 12, # ts gonna make the entire game unbalanced again
            "type" : "parry",
            "info" : "Buff the next attack to deal +4 damage. Additionally, gain an additional 50 percent chance to perform a perfect parry, reflecting all damage back to the attacker."
        },
        "BLAZING" : {
            "name" : "Blazing Wasteland",
            "style": "Fire",
            "cost" : 4,
            "power" : 15,
            "type" : "damage",
            "info" : "Heat up your weapon to deal 15 damage to a single enemy. Using this skill three times in a row will cause the user to burn out." # frick around and find out- in all seriousness, recoil dmg will be HALF the users hp
        },
        # implement later- i think were gonna have magic passives be included in the character data files instead
        "PASSIVE" : {
            "name" : "Bringer Of Light",
            "style" : "Fire", #or special idk
            "cost" : 999, # uh im just putting it as this bc i need to remember to fix this later
            "power" : 0, #plus burn dmg idk
            "type" : "magic-passive",
            "info" : "Automatically activate after using three FIRE spells in a single battle. When active, increase MAGIC intake by 1, and inrease AP by 1 for every additional FIRE spell cast." # ok this is just gonna be triton passive bc i dont wanna code another one in lol
        } # NOTE : NEED TO HAVE PASSIVE MAGIC INTAKE AS A CHAR TRAIT!!!!! !!!! PLS NOTICE TS FUTURE ME
    },
    "WATER" : {
        "FISH" : { # fih 
            "name" : "???",
            "style" : "UNKNOWN", # this one is just a troll spell (omg maybe i should make a few for debugging purposes ykyk??)
            "cost" : 0,
            "power" : 999,
            "type" : "one-time-use",
            "info" : "...You feel like clicking this spell would not help you progress." # toby fox annoying dog ahh
        },
        "DANCE" : {
            "name" : "Dancin' With The Dolphins",
            "style" : "Water",
            "cost" : 4,
            "power" : 12,
            "type" : "heal",
            "info" : "Dance with all your friends, and absorb all the good vibes coming from them to resotre VI."
        },
        "TIDE" : { # chat it is LOCK TF IN TIME!!! no actually i need to figure out enough spells to make them not just another button for attack (wish you could put in withering rose)
            "name" : "Tidal Force", #ok yeah idk why but my typing cursor is like 3 spaces ahead of where im typing wtf (pls help chat)
            "style" : "Water", #nvm chat i figured it out
            "cost" : 2,
            "power" : 6,
            "type" : "additional-attack",
            "info" : "Summon a large wave in the direction of your fishing rod, causing additional attacks to be more likely to occur for the next 3 TURNS." # PERLOS EXCLUSIVE (now i gotta go back and make EVERYBODY get exclusive attacks)
        },

        "PASSIVE" : {
            "name" : "BAM! 564 Fish!", # elite ball knowledge
            "style" : "Water", # yo i just realised, why am i putting the element in the style part if i already seperated by element earlier lmao
            "cost" : 999,
            "power" : 0,
            "type" : "magic-passive",
            "info" : "When casting any SPELL, gain a 30 percent chance to launch one additional attack with 50 percent of the original attack's damage. If the SPELL is a WATER type, increase the CRIT chance of the spell to 35."# NO THE CURSOR IS BROKEN AGAIN FML (ALSO NOTE TO SELF I FREAKING NEED TO ADD CRIT CHACNCE NOW ONGGGGGGGGG)
        }
    },
    # OMG WERE ON THE FUNNY CHUD DAD JOKER
    # ok i think it would be cool to have a no mercy/evil/bad route kinda for each, so im gonna do marchs first (bc theyre lowkey the dev test tool (thats why theyre op, bc i suck at my own game))
    "BLOOD" : {
        "TEAR" : {
            "name" : "A Tear For The Lost", #she gotta have the EMO names
            "style" : "Blood", # yeah im too far gone with the style stuff lol 
            "cost" : 4, # i want her to have higher spell costs since she IS meant to be a traditional attack spam until much later on (emo foreshadowing ah)
            "power" : 0,
            "type" : "buff",
            "info" : "This spell can only be cast after killing THREE enemies. Create a field, increasing all SPELL COST by 3, MAGIC REGEN by 1, and AP by 2. Stackable."
        },
        "SHRED" : {
            "name" : "Soul Shred",
            "style" : "Blood",
            "cost" : 3,
            "power" : 8,
            "type" : "damage",
            "info" : "Immediately deal 8 damage to an enemy, without ending your turn. For every enemy killed in this manner, gain +2AP."
        },
        "PUN" : {
            "name" : "A Vein Attempt", # AHAHAHAH TS SO FUNNY GUYS
            "style" : "Blood",
            "cost" : 7, #high cost bc itll be op or som
            "power" : 28, # yeah idk powerscaling, call tobias fox
            "type" : "damage",
            "info" : "Attempt to finish off an enemy. If the enemy is killed, gain RECKLESS. Otherwise, lose 5VI (If the VI COST exceeds current VI, set VI to 1)." #                                                                                         might add emotions? like "RECKLESS" which can incr atk and lower def??? im gonna put it in but ill check it later this is spaced out bc i dont need to be called emo
        },

        "JOKE" : {
            "name" : "B-Positive",
            "style" : "Blood",
            "cost" : 999,
            "power" : 0,
            "type" : "magic-passive",
            "info" : "After using a total of 10 MAGIC, heal 8 VI, gain +2AP and +2DP. All attacks now have a 30 percent chance to inflict BLEED. Additionally, every enemy killed has a 20 percent chance to cause an ADDITIONAL ATTACK."
        }
    },
    "ANIMAL" : {
        "FLUFFY" : {
            "name" : "Shield of Fluff",
            "style" : "Animal", 
            "cost" : 2,
            "power" : 2,
            "type" : "shield",
            "info" : "Using the power of sheep, cast a spell to increase DP. All attacks done by the enemy now have a chance to give the attacker the SLOW status." # 20 percent chance the attacker will miss their turn
        },
        "SPEEDY" : {
            "name" : "Fast Like a Rabbit",
            "style" : "Animal",
            "cost" : 2,
            "power" : 2,
            "type" : "buff",
            "info" : "Ask the rabbits for help, adding an extra turn for the user."
        },
        "OW" : {
            "name" : "Stompin' Time",
            "style" : "Animal",
            "cost" : 10,
            "power" : 8,
            "type" : "summon",
            "info" : "Summon one goat (named Bleet Bleet). Bleet Bleet will perform one additional attack for three turns, priorising the enemy with the least health. Only two Bleet Bleet's can be on field at the same time. (The first one is Bleet Bleet, the second one is Bleet Bleet Squared)."
        }
    },
    "WIND" : {
        "WIND" : {
            "name" : "Winds of Change",
            "style" : "Wind", 
            "cost" : 3
        }
    }
}
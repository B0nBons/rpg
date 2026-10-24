# were finally getting into the MAGIC w this one!!!!!
# I think were gonna seperate them by type (since i think im just doing 1mc per spell type)
# then itll be formatted with name,magic cost,buff/debuff, and a lil info blurb bc i love writing blurbs
# side note but why is my cursor not lining up with my typing wtf is codespaces even doin atp

spells = {
    "FIRE" : {
        "THERMAL SINK" :{ # lowk chat i got a cold
            "name" : "Thermal Sink",
            "style" : "Fire",
            "cost" : 3,
            "power" : 12, # ts gonna make the entire game unbalanced again
            "type" : "parry",
            "info" : "Buff the next attack to deal +4 damage. Additionally, gain an additional 50 percent chance to perform a perfect parry, reflecting all damage back to the attacker."
        },
        "BLAZING WASTELAND" : {
            "name" : "Blazing Wasteland",
            "style": "Fire",
            "cost" : 4,
            "power" : 15,
            "type" : "recoil",
            "info" : "Heat up your weapon to deal 15 damage to a single enemy. Using this skill three times in a row, or more than twice in a BOSS battle... (the text has been scratched out)" # frick around and find out- in all seriousness, recoil dmg will be HALF the users hp
        },
        "BRINGER OF LIGHT" : {
            "name" : "Bringer Of Light",
            "style" : "Fire", #or special idk
            "cost" : 100,
            "power" : 1000, #plus burn dmg idk
            "type" : "magic-passive",
            "info" : "Automatically activate after using three FIRE spells in a single battle. When active, increase MAGIC intake by 1, and inrease AP by 1 for every additional FIRE spell cast."
        }
    },
    "WATER" : {
        "FISH" : { # fih 
            "name" : "???",
            "style" : "UNKNOWN",
            "cost" : 0,
            "power" : 999,
            "type" : "one-time-use",
            "info" : "...You feel like clicking this spell would not help you progress."
        },
        "DANCE" : {
            "name" : "Dancin' With The Dolphins",
            "style" : "WATER",
            "cost" : 4,
            "power" : 12,
            "type" : "heal",
            "info" : "Dance with all your friends, and absorb all the good vibes coming from them to resotre VI."
        },
        "PLAVEHOLDBCIMMTIRED" : {
            
        }              
    }
}
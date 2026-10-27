# nobody comes for nhs tutoring at 820 am vro whys the advisor make me do this
# ok anyway we doing ECONOMY now
# also my game happens to match the antique them perfectly! only on terminal (im so smart (not lol))

# side note: decide what the currency will be- coins? gold???

from math import ceil # rounds to ceiling bc the merchants are stingyalso just learned its ceil not celi embarassing asf

def merchant_price(item, daily_sale = False):
    base_price = 0
    for location, items in BASE_PRICES.items:
        if item in items:
            base_price = items[item] # i never want to write if items in items items is item ever again what in the tongue twister >:(
            break # I LOVE BREAK STATEMENTS (my teacher in 8th grade said that if you had to use a break statement, ur code was ahh but i love using breaks)
    if daily_sale == True:
        return ceil(base_price * .8)
    # i think we can use up to 2 decimals(?) hmmmmmmmmmmmmmmmmmm idk lowkey thats future me issue
    elif daily_sale == False:
        return base_price # ok so i think 20 perent off might be a lil much but well see (guys if ur reading this pls gimme feedback)
        # i hope my comments bring joy to some reviewers life but also theres somebody screaming for bloody hell wtf is goin on
        
BASE_PRICES = {
    "FOREST" : {
        "WOOD" : 10, # common drop from not stationary trees
        "STONE" : 8, # drop from .....???? some random new enemy that ill add in the forest
        "BERRIES" : 1, # for a pack of 5 or som, each is .2?? common drop from all
        "MUSHROOM" : 16, # rare drop from toadstools
        "MOSS" : 3, # common drop from mossy toads
        "GHOST IN A BOTTLE" : 16,
        "CROCODILE SCALE" : 50 # the player should use the scale to craft a weapon or something
    } # the loot table WILL be revised later since i have a feeling somebody is gonna be a chud and grind everything out
}


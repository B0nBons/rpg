# ALRIGHT WE MAKING A BATTLE SYSTEM W THIS ONE
# ts gonna be hard isnt it
import random
from data.enemies import grab_forest

def checK_mc():
    pass

def forest_fight(char, boss=False):
    if boss:
        boss_enemy = grab_forest(True)
        enemy_stats = boss_enemy.copy()
    if not boss:
        enemy_stats = grab_forest(False).copy()

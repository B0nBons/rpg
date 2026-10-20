import time
import colorama

colorama.init(autoreset=True)

def protag_talk(text):
    for letter in text:
        print(colorama.Style.BRIGHT + letter, end='', flush=True)
        time.sleep(0.05)
    print("\n")
    return text

def typewriter(text, speed_s = 0.04):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(speed_s)
    print("\n")
    return text

# might change text based on current area (village is white, desert is yellow, jungle could be lime)
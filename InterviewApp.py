#---which mode--#
def modeSelect ():
    mode = input("Which mode would you like to use? (easy or hard)")
    mode2 = mode.lower()
    #easy-mode
    if mode2 == "easy":
        print("you chose easy lol wimp")
    #hard-mode
    elif mode2 == "hard":
        print("daayum hard")

modeSelect()

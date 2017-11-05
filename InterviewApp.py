#--------------------Demographics--------------#
#---Gender---#
def genderSelect ():

    while True:
        gender = input("What gender are you? (female, male, or other")
        gender2 = gender.lower()
        if gender2 == "female" or "male" or "other":
            break
        else:
            print("sorry, I didn't understand that. Please type either 'female', 'male', or 'other'

    
#---------------------Which Mode---------------#
def modeSelect ():
    mode = input("Which mode would you like to use? (easy or hard)")
    mode2 = mode.lower()
    #easy-mode
    if mode2 == "easy":
        print("you chose easy lol wimp")
    #hard-mode
    elif mode2 == "hard":
        print("daayum hard")

    #bad-choice
    else:
        print("Sorry,I didn't understand that. Please type either 'easy' or 'hard'") 

modeSelect()

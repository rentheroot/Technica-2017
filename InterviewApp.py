

#--------------------Demographics--------------#
#---Gender---#
def genderSelect (gender2):
    #while good input isn't given
    while True:
        gender = input("What gender are you? (female, male, or other)")

        gender2 = gender.lower()

        #if good input
        if gender2 == "female" or "male" or "other":
            return gender2
            break
        #if bad input
        else:
            print("sorry, I didn't understand that. Please type either 'female', 'male', or 'other'")

    
                  
#---------------------Which Mode---------------#
def modeSelect (mode2):
    while True:
        mode = input("Which mode would you like to use? (easy or hard)")
        mode2 = mode.lower()

        #if easy-mode
        if mode2 == "easy":
            print("you chose easy lol wimp")
            return mode2
            break
        #if hard-mode
        elif mode2 == "hard":
            print("daayum hard")
            return mode2
            break

        #if bad-choice
        else:
            print("Sorry,I didn't understand that. Please type either 'easy' or 'hard'") 
#--declare gender variable--#
gender2 = 0
mode2 = 0

#--print gender variable--#
gender2 = genderSelect(gender2)
print(gender2)

#--run mode select--#
mode2 = modeSelect(mode2)
print(mode2)

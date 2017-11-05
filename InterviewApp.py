

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

#---Race--#
def raceSelect (race2):
    #while good input isn't given
    while True:
        race = input("Please select the number that corresponds to your race" + '\n' + "1. American Indian or Alaska Native" + '\n' + "2. Asian" + '\n' + "3. Black or African American" + '\n' +"4. Hispanic or Latino" +'\n' + "5. Native Hawaiian or Other Pacific Islander" + '\n' + "6. White" +'\n') 

        race2 = race.lower()

        #if good input
        if race2 == "1" or "2" or "3" or "4" or "5" or "6":
            return race2
            break
        #if bad input
        else:
            print("sorry, I didn't understand that. Please type a number 1-6")
            
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
#--declare variables--#
gender2 = 0
mode2 = 0
race2 = 0

#--print gender variable--#
gender2 = genderSelect(gender2)
print(gender2)

#--run race select--#
race2 = raceSelect(race2)
print(race2)

#--run mode select--#
mode2 = modeSelect(mode2)
print(mode2)


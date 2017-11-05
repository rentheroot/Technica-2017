

#--------------------Demographics--------------#
#---Gender---#
def genderSelect (gender2):
    #while good input isn't given
    while True:
        gender = input("What gender are you? (female, male, or other)" + '\n')

        gender2 = gender.lower()

        #if good input
        if gender2 == "female" or gender2 == "male" or gender2 == "other":
            return gender2
            break
        #if bad input
        else:
            print("sorry, I didn't understand that. Please type either 'female', 'male', or 'other'" + '\n')

#---Race--#
def raceSelect (race2):
    #while good input isn't given
    while True:
        race = input("Please select the number that corresponds to your race" + '\n' + "1. American Indian or Alaska Native" + '\n' + "2. Asian" + '\n' + "3. Black or African American" + '\n' +"4. Hispanic or Latino" +'\n' + "5. Native Hawaiian or Other Pacific Islander" + '\n' + "6. White" +'\n') 

        race2 = race.lower()

        #if good input
        if race2 == "1" or race2 == "2" or race2 == "3" or race2 == "4" or race2 == "5" or race2 == "6":
            return race2
            break
        #if bad input
        else:
            print("sorry, I didn't understand that. Please type a number 1-6" + '\n')

#---State Select--#
def stateSelect (state2):

    #list of U.S. state abbreviations
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    while True:
        state = input("Please type in the 2 letter abbreviation for the U.S. state you live in" + '\n')
        state2 = state.upper()

        #if good input
        if state2 in states:
            return state2
            break
        #if bad input
        else:
            print("sorry, I don't understand what you are saying, Please type in the 2 letter abbreviation for the U.S. state you live in" + '\n')
               
#---------------------Which Mode---------------#
def modeSelect (mode2):
    while True:
        mode = input("Which mode would you like to use? (easy or hard)" + '\n')
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
            print("Sorry,I didn't understand that. Please type either 'easy' or 'hard'" + '\n') 
#--declare variables--#
gender2 = 0
mode2 = 0
race2 = 0
state2 = 0

#--print gender variable--#
gender2 = genderSelect(gender2)
print(gender2)

#--print state variable--#
state2 = stateSelect(state2)
print(state2)
#--run race select--#
race2 = raceSelect(race2)
print(race2)

#--run mode select--#
mode2 = modeSelect(mode2)
print(mode2)


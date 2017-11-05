#-- Imports --#
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
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
    #while good input isn't given
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
#--Age select--#
def ageSelect (age):
    while True:
        age = int(input("What is your age?" + '\n'))

        #if good input
        try:
            age += 1
            age -= 1
            return age
            break
        #if bad input
        except:
            print("sorry, I don't understand what you are saying. Please make sure you enter an integer for your age." + '\n')

#---Marital Status---#
def marriageSelect (marriage2):
    #while good input isn't given
    while True:
        marriage = input("What is your current marital status?(single, married, divorced, widowed" + '/n')

        marriage2 = marriage.lower()

        #if good input
        if marriage2 == "single" or marriage2 == "married" or marriage2 == "divorced" or marriage2 == "widowed":
            return marriage2
            break
        #if bad input
        else:
            print("sorry, I didn't understand that. Please type either 'single', 'married', 'divorced' or 'widowed'" + '\n')


#---Job Status---#
def jobSelect(job2):
    #while good input isn't given
    while True:
        job = input("What is your current job status?(unemployed, self-employed, non-profit, corporate, government, student)" + '\n')

        job2 = job.lower()

        #if good input
        if job2 == "unemployed" or job2 == "self-employed" or job2 == "non-profit" or job2 == "corporate" or job2 == "government" or job2 == "student":
            return job2
            break
        #if bad input
        else:
            print("sorry, I didn't understand that. Please type either 'unemployed', self-employed', 'corporate', or 'non-profit'" + '\n')    
               
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
age = 0
job2 =0
marriage2 = 0
documents = 0

#--print gender variable--#
gender2 = genderSelect(gender2)
print(gender2)

#--print age variable--#
age = ageSelect(age)
print(age)
#--print state variable--#
state2 = stateSelect(state2)
print(state2)
#--run race select--#
race2 = raceSelect(race2)
print(race2)

#-- print job variable--#
job2 =jobSelect(job2)
print(job2)

#-- print marriage variable
marriage2 = 0
print(marriage2)

#--run mode select--#
mode2 = modeSelect(mode2)
print(mode2)

#--Actual Stuff--#
# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the accessKey string value with your valid access key.
accessKey = 'ae905e07e77e4712ab74ebd1caee2f4a'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your access keys.
# For example, if you obtained your access keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial access keys are generated in the westcentralus region, so if you are using
# a free trial access key, you should not need to change this region.
uri = 'westus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/languages'

def getDocuments (documents):
    with open('jsonDocuments.json') as json_data:
        documents = json.load(json_data)
        return documents
    
def GetLanguage (documents):
    "Detects the languages for a set of documents and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()

##documents = { 'documents': [
##    { 'id': '1', 'text': 'This is a document written in English.' },
##    { 'id': '2', 'text': 'Este es un document escrito en Español.' },
##    { 'id': '3', 'text': '这是一个用中文写的文件' }
##]}

def returnResults ():
    
    print 'Please wait a moment for the results to appear.\n'

    result = GetLanguage (documents)
    print (json.dumps(json.loads(result), indent=4))

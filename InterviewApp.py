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
sentiment_path = '/text/analytics/v2.0/sentiment'
keyphrase_path = '/text/analytics/v2.0/keyPhrases'

def getDocuments ():
    with open('jsonDocuments.json', 'r') as json_data:
        documents = json.load(json_data)
        return documents
    
def GetLanguage (documents)):
    "Detects the languages for a set of documents and returns the information."

    print ('Please wait a moment for the results to appear.\n')

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    structured_doc = {'documents': [{'id': '1', 'language': 'en', 'text': documents}]}
    # Get sentiment
    conn.request ("POST", sentiment_path, structured_doc, headers)
    response = conn.getresponse().read()
    sentiment = response['documents'][0]['score']
    # Get key phrases
    conn.request("POST", keyphrase_path, structured_doc, headers)
    keyphrase_response = conn.get_response()
    keyphrases = keyphrase_response['documents'][0]['keyPhrases']
     
    return sentiment, keyphrases

##documents = { 'documents': [
##    { 'id': '1', 'text': 'This is a document written in English.' },
##    { 'id': '2', 'text': 'Este es un document escrito en Español.' },
##    { 'id': '3', 'text': '这是一个用中文写的文件' }
##]}

def returnResults (question):
    
    
    print (json.dumps(json.loads(result), indent=4))

def startUncomfortable():
    print('Welcome to the Uncomfortable survey\n')

#safeword is john cena

master_record = {}
    
def firedFromJob ():
    # Question string
    question_str = 'Have you ever been fired from a job? '
    # Get user input
    fired = input(question_str)
    # Submit use input to MS Cognitive etc. API
    sentiment, keyphrases = GetLanguage(fired)
    master_record['firedFromJob'] = {'question': question_str,
                                     'answer': fired}

    if ms_response.sentiment > 0.5
        yourFault()
    else:
        believeInGod()

    return
    
def yourFault():
     # Question string
    question_str = 'Was it your fault that you got fired? '
    # Get user input
    fault = input(question_str)
    # Submit use input to MS Cognitive etc. API
    sentiment, keyphrases = GetLanguage(fault)
    master_record['yourFault'] = {'question': question_str,
                                     'answer': fault}

    if ms_response.sentiment > 0.5
        believeInGod()
    else:
        weightOpinion()

    return

def believeInGod ():
    # Question string
    question_str = 'to what extend do you believe in god? '
    # Get user input
    belief = input(question_str)
    # Submit use input to MS Cognitive etc. API
    sentiment, keyphrases = GetLanguage(fired)
    master_record['firedFromJob'] = {'question': question_str,
                                     'answer': belief}

    if ms_response.sentiment > 0.5
        alienExistence()
    else:
        appearanceOpinion()

    return


def alienExistence ():
     # Question string
    question_str = 'Do you believe in aliens? '
    # Get user input
    aliens = input(question_str)
    # Submit use input to MS Cognitive etc. API
    sentiment, keyphrases = GetLanguage(aliens)
    master_record['alienExistence'] = {'question': question_str,
                                     'answer': aliens}

    if ms_response.sentiment > 0.5
        smashAlien()
    else:
        haremEnding()

    return

def smashAlien ():
    # Question string
    question_str = 'Would you smash an alien? '
    # Get user input
    smash = input(question_str)
    # Submit use input to MS Cognitive etc. API
    sentiment, keyphrases = GetLanguage(smash)
    master_record['smashAlien'] = {'question': question_str,
                                     'answer': smash}

    if ms_response.sentiment > 0.5
        wouldSmash()
    else:
        wouldNotSmash()

    return

def wouldSmash ():
    print('whatever youre into im not gonna judge\n')

        accidentallyCalledMom()
    return

def wouldNotSmash ():
    print('you have no sense of adventure smh\n')

        accidentallyCalledMom()
    return

def appearanceOpinion ():
   accidentallyCalledMom


def weightOpinion ():
    # Question string
    question_str = 'What is your opinion on your weight? '
    # Get user input
    weight = input(question_str)
    # Submit use input to MS Cognitive etc. API
    sentiment, keyphrases = GetLanguage(weight)
    master_record['weightOpinion'] = {'question': question_str,
                                     'answer': weight}

    if ms_response.sentiment > 0.5
        ratingAppearance()
    else:
        beautifulPotato()

    return

def beautifulPotato ():
    print('you are a beautiful potato\n')

def ratingAppearance ():
    print('id rate you a 2/10 if i was being generous\n')

#--Pt2--#

def accidentallyCalledMom ():
    print('Who was the last person you accidently called mom?')

        ratherMom()
    return

def ratherMom():
    # Question string
    question_str = 'Would you rather they be your mom instead of your actual mom? '
    # Get user input
    mom = input(question_str)
    # Submit use input to MS Cognitive etc. API
    sentiment, keyphrases = GetLanguage(mom)
    master_record['ratherMom'] = {'question': question_str,
                                     'answer': mom}

    if ms_response.sentiment > 0.5
        familyDeathReaction()
    else:
        lyingtoParents()

    return

def lyingtoParents ():
    # Question string
   print('Describe your feelings about the last time you lied to your parents? ')
   
        lyingToFriends()

    return


def lyingToFriends ();
    # Question string
    question_str = 'Do you feel worse about lying to close friends? '
    # Get user input
    worse = input(question_str)
    # Submit use input to MS Cognitive etc. API
    sentiment, keyphrases = GetLanguage(worse)
    master_record['lyingToFriends'] = {'question': question_str,
                                     'answer': worse}

    if ms_response.sentiment > 0.5
        afraidOfDeath()
    else:
        haremEnding()

    return

def haremEnding ():
   print('So if the time-space continuum warped and you were sent to a parallel dimension where it is customary to walk on your hands and the world was made of glazed donuts, and the only way home was to stop the great Zalief from stealing the Infinity Gem from the King of Trees by using the Cooler of Ancient Legends, how would you successfully disarm the bomb to get the harem ending?')

        destructionOfEarthandGalaxy
    return

def familyDeathReaction ():
   print('Describe how your family would feel if you died. ')

        afraidOfDeath()

    return

def afraidOfDeath ():
  print('are you afraid of death? ')

        destructionOfEarthandGalaxy
        
    return

def destructionOfEarthandGalaxy ();
    print(Briefly discuss the inevitable destruction of our universe as we percieve it. ')

        deepBeans()
    return

def deepBeans ():
    print('thats some deep beans my dude\n')

firedFromJob()

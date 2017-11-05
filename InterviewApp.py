#-- Imports --#
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

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
        documents = documents.encode('utf-8')
        return documents
    
def GetLanguage (documents):
    #"Detects the languages for a set of documents and returns the information."

    print ('Please wait a moment for the results to appear.\n')

    headers = {'Ocp-Apim-Subscription-Key': accessKey.encode}
    conn = http.client.HTTPSConnection (uri)
    documents2 = documents.encode('utf-8')
    structured_doc = {'documents': [{'id': '1', 'language': 'en', 'text': documents2}]}
    print(structured_doc)
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

#safeword is john cena (jk no safeword rip)

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

    if ms_response.sentiment > 0.5:
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

    if ms_response.sentiment > 0.5:
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

    if ms_response.sentiment > 0.5:
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

    if ms_response.sentiment > 0.5:
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

    if ms_response.sentiment > 0.5:
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

    if ms_response.sentiment > 0.5:
        ratingAppearance()
    else:
        beautifulPotato()

    return

def beautifulPotato ():
    print('you are a beautiful potato\n')

    accidentallyCalledMom ()
    return
def ratingAppearance ():
    print('id rate you a 2/10 if i was being generous\n')
    
    accidentallyCalledMom ()
    return
#--Pt2--#

def accidentallyCalledMom ():
    # Question string
    question_str = 'Who was the last person you accidently called Mom? '
    # Get user input
    oopsmom = input(question_str)
    # Submit use input to MS Cognitive etc. API
    sentiment, keyphrases = GetLanguage(oopsmom)
    master_record['accidentallyCalledMom'] = {'question': question_str,
                                     'answer': oopsmom}

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

    if ms_response.sentiment > 0.5:
        familyDeathReaction()
    else:
        lyingtoParents()

    return

def lyingtoParents ():
    # Question string
    question_str = 'Describe your feelings about the last time you lied to your parents. '
    # Get user input
    lying = input(question_str)
    # Submit use input to MS Cognitive etc. API
    sentiment, keyphrases = GetLanguage(lying)
    master_record['lyingtoParents'] = {'question': question_str,
                                     'answer': lying}
    lyingToFriends()

    return


def lyingToFriends ():
    # Question string
    question_str = 'Do you feel worse about lying to close friends? '
    # Get user input
    worse = input(question_str)
    # Submit use input to MS Cognitive etc. API
    sentiment, keyphrases = GetLanguage(worse)
    master_record['lyingToFriends'] = {'question': question_str,
                                     'answer': worse}

    if ms_response.sentiment > 0.5:
        afraidOfDeath()
    else:
        haremEnding()

    return

def haremEnding ():
   question_str = 'So if the time-space continuum warped and you were sent to a parallel dimension where it is customary to walk on your hands and the world was made of glazed donuts, and the only way home was to stop the great Zalief from stealing the Infinity Gem from the King of Trees by using the Cooler of Ancient Legends, how would you successfully disarm the bomb to get the harem ending? '
    # Get user input
   harem = input(question_str)
   # Submit use input to MS Cognitive etc. API
   sentiment, keyphrases = GetLanguage(harem)
   master_record['haremEnding'] = {'question': question_str,
                                     'answer': harem} 
   destructionOfEarthandGalaxy ()
   return

def familyDeathReaction ():
   # Question string
    question_str = 'Describe how your family would feel if you died? '
    # Get user input
    feel = input(question_str)
    # Submit use input to MS Cognitive etc. API
    sentiment, keyphrases = GetLanguage(feel)
    master_record['familyDeathReaction'] = {'question': question_str,
                                     'answer': feel}

    afraidOfDeath()

    return

def afraidOfDeath ():
  # Question string
    question_str = 'Are you afraid of death? '
    # Get user input
    fear = input(question_str)
    # Submit use input to MS Cognitive etc. API
    sentiment, keyphrases = GetLanguage(fear)
    master_record['afraidOfDeath'] = {'question': question_str,
                                     'answer': fear}
    destructionOfEarthandGalaxy ()
        
    return

def destructionOfEarthandGalaxy ():
    # Question string
    question_str = 'Briefly discuss the inevitable distruction of our universe as we know it. '
    # Get user input
    crisis = input(question_str)
    # Submit use input to MS Cognitive etc. API
    sentiment, keyphrases = GetLanguage(crisis)
    master_record['destructionOfEarthandGalaxy'] = {'question': question_str,
                                                     'answer': crisis}

    deepBeans()
    return

def deepBeans ():
    print('thats some deep beans my dude\n')

    with open('master_file.json', 'w') as json_file:
      json.dump(master_record, json_file)

firedFromJob()

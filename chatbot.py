import random
import webbrowser
import re
name="ABHIK"
weather="windy"
nameq="what is my name?"
NAMES_INPUT=['ABHIK','MURARI','RAMVEER','LITORIYA']
CITY_INPUTS=['AGRA','LUCKNOW','DELHI','MUMBAI']
CITY_QUERY=['where are we','guess my city','tell my city', 'where should i go to', 'city']
PERCEPTS_SEQUENCE={'google': 'https://www.google.com', 'facebook' : 'https://www.facebook.com','microsoft': 'https://www.microsoft.com','twitter': 'https://www.twitter.com','discord': 'https://www.discord.com'}

GREETING_INPUTS = ("hello", "hi","what's up","hey","how are you?")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad"]

UNKOWN_RESPONSES = ["I don't understand", "Sorry, can't help with that","Please be more clear!!"]
class response:
    
    def greeting(sentence):
    #"""If user's input is a greeting, return a greeting response"""
        for word in sentence.split():
            if word.lower() in GREETING_INPUTS:
                return random.choice(GREETING_RESPONSES)

    def undefined(user_response):
        return random.choice(UNKOWN_RESPONSES)

    def reflection(user_refection):
        pass

class Agent:
     def __init__(self):
        flag=True
        print("BOB: My name is BOB. Ask me anything. If you want to exit, type Bye!")
        while(flag==True):
            user_response = input()
    
            user_response=user_response.lower()
            if(user_response!='bye'):
                if(user_response=='thanks' or user_response=='thank you' ):
                    flag=False
                    print("BOB: You are welcome "+name)
                else:
                    if(response.greeting(user_response)!=None):
                        print("BOB: "+response.greeting(user_response))
                    elif(user_response.__eq__(nameq) or user_response.__eq__("who am i ?") or user_response.__eq__("Do you know me") or user_response.__eq__("tell my name")):
                        print("BOB: You are "+name)
                    elif(user_response in CITY_QUERY):
                        print("BOB: "+random.choice(CITY_INPUTS))
                    elif((user_response in CITY_QUERY) and ('my' or 'i' or 'me' or 'myself' in user_response) ):
                        print("BOB: AGRA")
                    elif(user_response in PERCEPTS_SEQUENCE):
                        print("BOB: opening "+user_response+".com")
                        webbrowser.open('http://'+user_response+'.com')
                    elif(re.findall('\d+? *?\+ *?\d+?',user_response)):
                        print("BOB: Answer is ")
                        print (eval(user_response))
                    else:
                        print("BOB: ",end="")
                        print(response.undefined(user_response))
            else:
                flag=False
                print("BOB: Bye! "+name+" take care..")

def TableDrivenVacuumAgent():
    table = {((),): 'Right',
             ((loc_A, 'Dirty'),): 'tuck',
             ((loc_B, 'Clean'),): 'Left',
             ((loc_B, 'Dirty'),): 'uck',
             ((loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
             ((loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
             # ...
             ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
             ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
             # ...
             }
    return TableDrivenAgent(table)
chat=Agent()


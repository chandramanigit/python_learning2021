# final version1.1 added to accomdate Noun 
#final version 1.2 statement 
# A student discovered another issue with the program. 
# The program cannot return the definition of acronyms such as USA or NATO; 
# therefore, add another conditional to make the program return the definition of such words. 

import json
from difflib import get_close_matches  #difflib module 
with open("App1_Building_Dictionary\\data.json" , "r") as myfile:
    raw_data=json.loads(myfile.read())
# better approch is to use json.load file instead of json.loads content   
'''
raw_data=json.load(open("App1_Building_Dictionary\\data.json"))
'''

def interactive():
    query= input("Enter Word: ").lower()  #lower case only 
    if query in raw_data.keys():
        return "\n".join(raw_data[query])  #list joining method
    elif query.title() in raw_data.keys():              #final version added 
        return "\n".join(raw_data[query.title()])  #list joining method
    elif query.upper() in raw_data.keys():              #final version added 
        return "\n".join(raw_data[query.upper()])  #list joining method
    elif len(get_close_matches(query , raw_data.keys())) > 0:
        yn= input("did you mean %s instead? Enter Y for yes , or N if no: " % get_close_matches(query,raw_data.keys())[0])
        if yn == "Y":
            return "\n".join(raw_data[get_close_matches(query,raw_data.keys())[0]])
        elif yn == "N":
            return "The word doesn't exist , please double check it"
        else:
            return "I could not understand your query !!"
    else:
        return "The word doesn't exist , please double check it"

print(interactive())    

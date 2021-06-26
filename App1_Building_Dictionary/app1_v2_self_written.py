import json
with open("App1_Building_Dictionary\\data.json" , "r") as myfile:
    raw_data=json.loads(myfile.read())
   
def interactive():
    query= input("Enter Word: ")
    if query in raw_data.keys():
        return "\n".join(raw_data[query])  #list joining method
    else:
        return "The word doesn't exist , please double check it"
        #print(*result , sep = '\n')

print(interactive())    
import json
with open("App1_Building_Dictionary\\data.json" , "r") as myfile:
    raw_data=json.loads(myfile.read())
   
def interactive():
    query= input("Enter Word: ")
    if query in raw_data.keys():
        return str(raw_data["query"])

print(interactive())
    
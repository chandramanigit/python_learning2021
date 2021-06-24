def sentence_make(phrase):
    capitalized = phrase.capitalize()
    interrogative = ("how" , "what" , "when" , "why")
    if phrase.startswith(interrogative):
        return "{} ?".format(capitalized)
    else:    
        return "{}.".format(capitalized) 
    
result = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        result.append(sentence_make(user_input))
    
print(" ".join(result)) #result fff


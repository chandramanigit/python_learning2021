'''
file = open("test.txt")
content = file.read(10)
print(content)
file.close()


def readfile(character , filepath ):
    print(filepath , character)
    myfile = open(filepath)
    content = myfile.read()
    myfile.close()
    return content.count(character)
'''
import json
with open("test.txt" , "a+") as sourcefile:
    sourcefile.seek(0)
    content = sourcefile.read()
    #sourcefile.write(content)
    #sourcefile.write(content)
    print((content.splitlines()[-1:][0]))
    

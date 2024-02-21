#WAP to create a dictionary of hindi words with values as their english translation.Provide user with an option to look it up!
myDict = {
    "pankha" : "fan",
    "maafi" : "sorry",
    "dabba" : "box"
    }
print("available hindi words are : ",myDict.keys())
a = input("Enter the hindi word\n")
#print("the translation is : ",myDict[a])

print("the translation is : ",myDict.get(a))
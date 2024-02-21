Mydictionary = {
    "BATMAN"  : "bruce wayne",
    "IRONMAN" : "tony stark",
    "captain": "steve rogers",
    "scores" : [1,2,3],#list insertion is also possible
    "dict-inside-dict" : {
        "MARVELS" : "avengers",
        "DC" : "justice league"
        }#nested dictionary
}

print(Mydictionary['BATMAN'])
print(Mydictionary["captain"])

Mydictionary["scores"] =[4,5,6]#updation is possible
print(Mydictionary['scores'])

print(Mydictionary["dict-inside-dict"]["MARVELS"])
print(Mydictionary["dict-inside-dict"]["DC"])
#print(Mydictionary)


###note : keys unique hona zaroori hai ,values unique hona nahi


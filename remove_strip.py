#write a python function to remove a given word from a string and strip it at the same time
#meaning of "strip" is to remove extra spaces around a string

def remove_strip(string,word):
    newstr = string.replace(word,"")
    return newstr.strip()

Intro = "              hello i'm harry the coder            "

a = remove_strip(Intro,"hello")
print(a)
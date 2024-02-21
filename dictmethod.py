mydict = {
    "fast" : "in a quick manner",
    "harry" : "youtuber",
    "marks" : [1,2,5],
    "anotherdict":{'harry':'player'},
    1:2
}

#methods
print(list(mydict.keys()))#prints all keys
print(mydict.values())#prints all values 
print(mydict.items())#prints all the (key,values)

print(mydict)
updatedict = {
    "hunny":"friend",
    "bunny":"not friend",
    "harry":"teacher"#purani values ko bhi update kr dega
    
}
mydict.update(updatedict)
print(mydict)

#python asked interview question on the below concept
print(mydict.get("harry"))
#or
print(mydict["harry"])
#upper both works

#but if
print(mydict.get("harry2"))#will return none
#while
# print(mydict["harry2"])#will throw error

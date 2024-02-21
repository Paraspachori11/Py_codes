#below given line will not generate an empty set
#it'll generate an empty dictionary
a = {}
print(type(a))

#actual way of generating empty set
b = set()
print(type(b))

##methods
##1)
#adding elements in empty set
b.add(1)
b.add(5)
#if we add previously added elements like 1 or 5 again , then it will not increase the number of occurences in the set
print(b)

#note : set mai unhashable types ko add nahi kr sakte hain

#b.add([4,5,6])#can't add cause LIST is unhashable type

b.add((4,5,6))#but tuple could be added to set
print(b)

#b.add({"asus":"TUF"})#dictionary also can't be added

##2)
print(len(b))

##3)
b.remove(5)
#b.remove(15) #don't remove such things that are not present in the set,otherwise you'll receive error
print(b)

##4)
print(b.pop())#this method will randombly take out an element out of the set and return remove element to you 
print(b)
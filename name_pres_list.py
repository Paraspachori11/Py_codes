#WAP which finds out whether a given name is present list or not

list = ["abc","bcd","cde","def","efg"]
name = input("enter the name you want to search : ")

if name in list:
    print("YES it's present in the list")
else:
    print("NO it's abscent in the list")
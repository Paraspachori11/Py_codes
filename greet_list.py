#WAP to greet all the person name stored in a list l1 and which starts with S 
#              l1 = ["harry","Sam","Sachin","rahul"]  

l1 = ["harry","Sam","Sachin","rahul"]
for name in l1:
    if name.startswith("S"):
        print("Hello "+name)
#WAP to find whether a given username contains less than 10 charaters or not

un = input("ENter USERNAME ")
lun = len(un)

if(lun<10):
    print(lun ,"number of charcters are present")
    print("& Are less than 10 characters")
else:
    print(lun,"number of characters i.e more than 10 are present")
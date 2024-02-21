L = [1,2,34,8,16,32,64,128,256,512,1024,32768,65536,4294967296]

mydict={}
for i in L:
    if(len(str(i))) in mydict:
        mydict[len(str(i))].append(i)
    else:
        mydict[len(str(i))]=[i]

print(mydict)

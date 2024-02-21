# #WAP to print the content of a list
# 
# ##WHILE LOOP


a = ["a","b","c","d","e","f","g","h","i","j","k","k","l","m","n","o","p","q","r","s","t","u","v","w","x","x","y","z"]
i = 0
while i<len(a) :
    print(a[i])
    i = i+1

##FOR LOOP

a = ["a","b","c","d","e","f","g","h","i","j","k","k","l","m","n","o","p","q","r","s","t","u","v","w","x","x","y","z"]

for item in a:
    print(item)

###RANGE function 

# for printing from 0th index
for i in range(8):
    print(i)

# for printing from 1st index  
for i in range(1,8):
    print(i)

#for step sizeing
for i in range(1,8,2):
    print(i)

#for with else
for i in range(10):
    print(i)
else :
    print('loop termination completed')

#break statement
for i in range(10):
    if i==5:
        break
    print(i)
    
else :
    print('loop termination completed')

#continue statement (jis value k liye continue likha hai usey skip karke aage bhad jaayega agli value k liye)
for i in range(10):
    if i==5:
        continue
    print(i)

#pass statement(i.e for not doing task completion at present time and should be done in the future)
i = 4

if i>0:
    pass
while i>6:
    pass
print("harry is a good boy")
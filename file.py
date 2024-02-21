#procedure

f = open('system.txt','r')#here 'system.txt' -> file to be opened & 'r' -> mode of opening file(here it's opened in read mode)
#f = open('system.txt')   #defaultly, it'll open in read move & #if a file is not present , then it'll get created
data = f.read()           #read the complete file
#data = f.read(2)         #read 2 characters from the text
print(data)               #print the file
f.close()                 #closing the file


#readline function

f = open('system.txt','r')
#prints 1st line of file
data = f.readline()
print(data)
#prints 2nd line of file
data = f.readline()
print(data)
#prints 3rd line of file and so on...
data = f.readline()
print(data)
f.close()

#append mode
f = open('another.txt','a')#this time using of append mode
f.write("i'm appending")#jitni baar program run karunga ,utni hi baar woh list k end mai judta chala jaayega
f.close()

#write mode
f = open('another.txt','w')
f.write("i'm writing")
f.close()

#with statement(bests way to open and close the file automatically)

with open('another.txt','r') as f:
    print(f.read())
with open('another.txt','w') as f:
    a = f.write("i'm still writing")
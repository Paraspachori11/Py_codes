#A file contains a "Donkey" multiple times .you need to write a program which replaces this word with ##### by updating the same file.

with open('system.txt') as f:
    a = f.read()

a = a.replace('donkey','#######')

with open('system.txt','w') as f:
    f.write(a)

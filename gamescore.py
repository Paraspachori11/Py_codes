#The game() function in a program lets a user play a game and returns the score as an integer .
#you need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score.
#You need to write a program  to update the Hiscore whenever game() breaks the Hi-score.

def game():
    return 45
g = game()

f = open('Hi-score.txt','r')                 # here a = represents Hi-score
a = f.read()                                 #      g = represents current-score
print(str(g) +" is the current score" )

if a=='':
    with open('Hi-score.txt','w') as f:
        f.write(str(g))
        
elif int(a)<g :
    with open('Hi-score.txt','w') as f:
        f.write(str(g))                      #important observation --> iss line mai 'str' use na karne pe program ek baar chalke value ko erase kar rha hai uski txt file se
elif int(a)>=g:
    with open('Hi-score.txt','w') as f:
        f.write(a)
f.close()
with open('Hi-score.txt') as f:
    hiscore = f.read()
    print(hiscore + " is  now the Hi-score")

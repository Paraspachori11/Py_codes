#                                                          SNAKE,WATER,GUN(GAME)
import random

def game(comp,you):
    if comp ==you:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you =="g":
            return False
        elif you =="s":
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you =="w":
            return True



print("computer's turn: snake(s) water(w) gun(g)")
randno = random.randint(1,3)

if randno == 1:
    comp = "s"
elif randno == 2:
    comp = "w"
else :
    comp = "g"




you = input("player's turn: snake(s) water(w) gun(g)")


a = game(comp,you)
print("computer has chosen")
print(comp)
if a ==None:
    print("IT'S a TIE")
elif a:
    print("YOU WIN")
else:
    print("YOU LOSE")
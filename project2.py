#************************************************ THE PERFECT GUESS ****************************************************************************

# We are going to write a program that generates a random number and asks the user to guess it .
# If the player's guess is higher than the actual number,the program displays " Lower number please ".
# similarly , if the user's guess is too low , the program prints " higher number please "
# when the user guesses the correct number , the program displays the number of guesses the player used to arrive at the number .

# HINT : Use the random module

import random
randnumber = random.randint(1,100)
#print(randnumber)
userGuess = None
guesses = 0

while(userGuess != randnumber):
    userGuess = int(input("Enter the number\n"))
    guesses += 1
    if userGuess==randnumber:
        print("you guessed it right")
    else:
        print("you guessed it wrong")
        if userGuess>randnumber:
            print("ENter a smaller number ")
        else: 
            print("enter a greater number")
        

print(f"you've guessed the correct number in {guesses} guesses")
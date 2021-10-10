import random

number = random.randint(1 , 9)
chances = 0
print("Number Guessing Game")
print("Guess a number (between 1 to 9)")

while chances<5 :
    guess = int(input("Enter your guess :"))

    if(guess == number) :
        print("Congratulations!! You won the game")
        break

    elif guess<number :
        print ("Your guess is too low guess a number higher than " , guess)
    else:
        print("Your guess is too high , please guess lower than ", guess)
    
    chances+=1


if not chances < 5 :
    print("You lose ☹, the number was ",number)
    

    
    
 


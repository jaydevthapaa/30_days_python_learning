# while loop 

# printing the multiplication of number by taking user input

num= int(input("enter the number: "))
i=1

while i<=10:
    print(num *i)
    i+=1
    
    
# guessing game in python
import random

jackpot = random.randint(1,100)
guess= int(input("GUESS THE NUMBER: "))
counter =1

while guess!= jackpot:
    if guess<jackpot:
        print("Guess higher number than that: ")
    else:
        print("guess lower number than that: ")
    
    guess= int(input("GUESS THE NUMBER again: "))
    counter+=1
    
print("right answer you can enjoy")
print("you guessed the number in: ", counter, "attempts keep it up")
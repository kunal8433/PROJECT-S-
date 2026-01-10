import random
"""Guess the number game"""

guess =  random.choice([1,100])
print("WELCOME TO KUNAL MALIK GAME")
print()
you = int(input("Guess your choice:"))

if guess == you:
        print("Your guess is Correct!")
        
else:
        if guess >= you:
           print("Guess Low Number:")
           
        elif guess <= you:
           print("Guess High Number")
           
                    

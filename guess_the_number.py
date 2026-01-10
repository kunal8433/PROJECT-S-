import random
"""Guess the number game"""

guess =  random.choice([1,100])
print("WELCOME TO ANGEL MALIK GAME")
print()
you = int(input("Guess your choice:"))
while True:

      if guess == you:
        print("Your guess is Correct!")
        
      else:
        if guess >= you:
           print("Guess Low Number:")
           
        elif guess <= you:
           print("Guess High Number")
           break
                    

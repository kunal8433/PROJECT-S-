import random
number = random.randint(1, 100)
while True:
    
    guess = int(input("Guess the valid number b/t 1 to 100:"))
    if guess == number:
        print("Congratulations! You guessed it right.")
        break
    else: 
          if guess < number:
             print("Too low! Try again.")
          elif guess > number:
                              print("Too high! Try again.")
          else:
                    print("Invalid number Try again.")
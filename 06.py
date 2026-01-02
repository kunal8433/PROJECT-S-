print("🎲 Welcome to Number Guessing Game 🎲")
print("I have a number between 1 and 100. Can you guess it?")

# Secret number (hidden in code)
secret_number = 42  
guess = None
attempts = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too Low! 📉 Try again.")
    elif guess > secret_number:
        print("Too High! 📈 Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} tries.")

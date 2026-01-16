print("Word Guessing Game 🧠")

word = "code"
guessed = ""
tries = 5

while tries > 0:
    letter = input("Guess a letter: ")

    if letter in word:
        guessed += letter
        print("Good guess 👍")
    else:
        tries -= 1
        print("Wrong guess ❌, Tries left:", tries)

    done = True
    for ch in word:
        if ch not in guessed:
            done = False

    if done:
        print("You guessed the word 🎉:", word)
        break

if tries == 0:
    print("Game Over 😢, Word was:", word)

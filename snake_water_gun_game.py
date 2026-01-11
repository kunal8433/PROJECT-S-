import random

'''
1 for gun
2 for water
3 for snake
'''

while True:
    computer = random.choice([1, 2, 3])

    yourstr = input("Enter your choice (g/w/s) or q to quit: ").lower()

    if yourstr == "q":
        print("Game Over! Thanks for playing 😊")
        break

    yourdict = {"g": 1, "w": 2, "s": 3}
    maindict = {1: "gun", 2: "water", 3: "snake"}

    if yourstr not in yourdict:
        print("Invalid input! Please choose g, w, or s.")
        continue

    you = yourdict[yourstr]

    print(f"\nYour choice: {maindict[you]}")
    print(f"Computer choice: {maindict[computer]}")

    if computer == you:
        print("MATCH DRAW!")
    
    elif (
        (computer == 1 and you == 2) or   # gun vs water → water wins
        (computer == 2 and you == 3) or   # water vs snake → snake wins
        (computer == 3 and you == 1)      # snake vs gun → gun wins
    ):
        print("YOU WIN!")
    
    else:
        print("YOU LOSE!")

    print("-" * 30)
    print()
import random

while True:
    choice = input("Rolling a Dice? (y/n): ")

    if choice == "y":
        computer = random.choice([
            (1,2),(3,4),(5,6),
            (1,3),(2,4),(5,1),
            (6,2),(3,5),(4,6)
        ])
        print("Dice rolled:", computer)

    elif choice == "n":
        print("Thank you")
        break   # loop stop ho jayega

    else:
        print("Invalid Choice")

import random
computer = random.choice([
      (1,2),(3,4),(5,6),(1,3),(2,4),(5,1),(6,2),(3,5),(4,6)])
choice = input("Rolling a Dice ? (y/n):")
while True:
        
        if choice == "y":
            print(computer)
        elif choice == "n":
             print("Thank you")
        else :
             print("Invalid Choice")
import random
'''
r for rock 
p for paper 
s for seasor
'''
computer = random.choice([1,2,3])
yourstr = input("Enter your choice:")
yourdict = {"r":1,"p":2,"s":3}
maindict = {1:"rock",2:"paper",3:"seasor"}

you = yourdict[yourstr]

print(f"You chose {maindict[you]}/n computer chose {maindict[computer]}")

if computer == you:
   print("Match Draw!")
else:
   if you == 1 and  computer == 2 :
        print("You Win!")
   elif you == 1 and  computer == 3 :
        print("You loss!")
   elif you == 2 and  computer == 3 :
        print("You loss!")
   elif you == 2 and  computer == 1 :
        print("You Win!")
   elif you == 3 and  computer == 1 :
        print("You Win!")
   elif you == 3 and  computer == 2 :
        print("You loss!")
   else:
        print("Something went wrong!")

    
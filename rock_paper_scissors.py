import random
'''
     1 for rock 
         2 for paper
            3 for scissors
                '''
computer = random.choice(
                           [
                               1
                                    ,
                                    2
                                    ,
                                 3
                                       ]
                                       
                                       )
print("Welcome to Rock , Paper , Scissors Game")    
print()
youstr = input("Enter your choice Rock , Paper , Scissors (r/p/s): ")
youdict = {"s":1 , "p" : 2 , "r":3}
maindict = {1:"Scissors" , 2:"Paper" , 3:"Rock"}

you = youdict[youstr]

print(f"you chose {maindict[you]} /n computer chose {maindict[computer]}")

if you == computer:
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

    
import random 
'''
g,1 for gun
s,2 for snake 
w,3 for water 

'''

computer = random.choice([1,2,3])
yourstr = input("Enter your choice g/s/w:")
yourdict = {
               "s"
                   :2
                       , "g" 
                             :1 
                                  ,
                                       "w"
                                            :3}

maindict = { 
            2:
               "snake"
                     ,  3:
                            "water",
                                      1:
                                          "gun"}
you = yourdict [yourstr]

print(f"You chose{maindict[you]} /n computer chose {maindict[computer]}")

if computer == you :
    print("MATCH DRAW!")

else:
    if computer == 1 and you == 2 :
        print("YOU LOSS")
    elif computer == 1 and you == 3 :
        print("YOU LOSS")
    elif computer == 2 and you == 1 :
        print("YOU WIN")
    elif computer == 2 and you == 3 :
        print("YOU LOSS")
    elif computer == 3 and you == 1 :
        print("YOU WIN")
    elif computer == 3 and you == 2 :
        print("YOU WIN")
    else:
        print("ERROR")
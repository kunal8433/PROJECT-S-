import random 
'''
1 for snake
0 for gun
-1 for water
'''

computer = random.choice([-1,0,1])
print("Welcome to Snake Water Gun Game")
print("s for snake \nw for water \ng for gun")
youstr = input("Enter your choice:")
youdict = {
              "s":1,
                 "w":-1,
                     "g":0 
                     
                     }
ComputerDict = { 
                1:"Snake"
                     ,-1:"Water",
                     
                            0:"Gun"
                       }

you = youdict[youstr]

print(f"You chose {youdict[youstr]}\nComputer chose {ComputerDict[computer]}")  # IMPORTANT

if( computer == 
                  you ):
    print("match draw")

else: 
    
    if(computer ==-1 and you ==1):
        print("YOU WIN!")

    elif(computer ==-1 
                      and you ==0):
        
        print("YOU  WIN!")

    elif(computer ==1  
                and you ==-1 ):
        print("YOU LOSS")

    elif(computer ==1
         
         
                 and you ==0):
        print("YOU WIN!")

    elif(computer ==0 and you ==-1):
        print("YOU WIN!")

    elif(computer ==0 and you ==1):
        print("YOU WIN!")
    
    else:
        print("something went wrong")


    





import random 
n = random.randint(1, 100)
print("WELCOME TO KUNAL MALIK GUESS NAME!")
print()
a =-1
gusses = 0
while(a!=n):
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower number plss")
        gusses +=1
    elif(a<n):
        print("Higher number plss")
        guesses +=1

print(f"You have guess the number {n} correctly {gusses} attempts")



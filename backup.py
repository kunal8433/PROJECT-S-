def add(x, y):
    return x+y

def subtract(x , y):
    return x - y 

def multiply (x , y ):
    return x * y

def Divide (x , y):
    if y == 0 :
        return "error"
    return x / y

print("select option")
print()
print("1.Addition")
print("2.subtract")
print("3.Divide")
print("4.multiply")
print()

choice = input("Enter your choice:")

num1  = float(input("Enter your number 1:"))
num2 = float(input("Enter your number 2:"))

if choice == '1':
    print("Result:", add (num1 , num2))
else:
    if choice == '2':
       print("Result:",subtract(num1 , num2 ) )
    elif choice == '3':
       print("Result:" , Divide(num1 , num2 ) )
    elif choice == '4':
       print("Result:", multiply(num1 , num2 ) )
    else:
      print("Error , something went wrong")

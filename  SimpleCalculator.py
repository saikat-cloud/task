

def add(x,y):
    return x + y

def subtrect(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("Select Your Operation")
print("1 . Add")
print("2 . Subtract")
print("3 . Multiply")
print("4 . Divide")

while True:
    select = input("Enter select (1/2/3/4): ")

    if select in ("1","2","3","4"):
        try:
            # float/int
            n1 = int(input("Enter First Number : "))
            n2 = int(input("Enter Secend Number: "))

        except ValueError:
            print("Invalid Input. Please Enter Number.")
            continue

        if select == "1":
            print (n1, "+", n2,"=", add(n1,n2))

        elif select == "2":
            print (n1, "-", n2, "=", subtrect(n1,n2))

        elif select == "3":
            print (n1, "*", n2, "=", multiply(n1,n2))

        elif select == "4":
            print (n1, "/", n2, "=", divide(n1,n2))

        nex = input ("let's Do Next Calculation? (yes/no): ")
        if nex == "no":
            break
    

    else:
        print("Invalid Input. Please Enter Number.")













# def reg(name,roll,age,cls):
#     return name + " is registerd and your roll is "+ roll + "your class is " + cls+ " your age is " + age 

# regs = reg("riyad", "10", "11","10")
# print(regs)




# # This function adds two numbers
# def add(x, y):
#     return x + y

# # This function subtracts two numbers
# def subtract(x, y):
#     return x - y

# # This function multiplies two numbers
# def multiply(x, y):
#     return x * y

# # This function divides two numbers
# def divide(x, y):
#     return x / y


# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# while True:
#     # take input from the user
#     choice = input("Enter choice(1/2/3/4): ")

#     # check if choice is one of the four options
#     if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))

#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))

#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))

#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
        
#         # check if user wants another calculation
#         # break the while loop if answer is no
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#           break
#     else:
#         print("Invalid Input")



def add(x,y):
    return x + y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print('Select your operation')
print('1 . Add')
print('2 . Subtract')
print('3 . Multiply')
print('4 . Divide')

while True:
    select = input('Select 1/2/3/4')

    if select in ('1','2','3','4'):
        try:
            num1 = float (input('Enter your first number'))
            num2 = float (input("Enter your secend number"))

        except ValueError:
            print('invalid input, please enter number')
            continue

        if select == '1':
            print(num1, '+', num2, '=', add(num1,num2))

        elif select =='2':
            print(num1, '-', num2, '=', subtract(num1,num2))

        elif select =='3':
            print(num1, '*', num2, '=', multiply(num1,num2))

        elif select =='4':
            print(num1, '/', num2, '=', divide(num1,num2))

        nex = input ('lets do next calculation? (yes/no)')
        if nex == 'no':
            break
    
    else:
        print("Invalid Input. Please Enter Number.")
    


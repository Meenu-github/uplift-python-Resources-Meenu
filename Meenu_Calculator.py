# The definition of the Addtion function

def add(num1, num2):
    return num1 + num2

# The definition of the Substraction function


def substract(num1, num2):
    return num1 - num2

# The definition of the multiply function


def multiply(num1, num2):
    return num1 * num2

# the definition of the divied function


def divide(num1, num2):
    return num1 / num2

# the definition of the modulo function


def modulo(num1, num2):
    return num1 % num2


print("Calculator")
print("Write 1 for Addition, 2 for Substraction, 3 for Multiplication, 4 for Division, 5 for Modulo")
choice = int(input("Enter your choice:  "))
first_num = float(input("Enter the First Number:  "))
second_num = float(input("Enter the second Number:  "))
if(choice == 1):
    print(add(first_num, second_num))
if(choice == 2):
    print(substract(first_num, second_num))
if(choice == 3):
    print(multiply(first_num, second_num))
if(choice == 4):
    print(divide(first_num, second_num))
if(choice == 5):
    print(modulo(first_num, second_num))
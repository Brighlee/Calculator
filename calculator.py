

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

choice = int(input("Enter your choice: "))

if choice == 1:
    result = add(num1, num2)
elif choice == 2:
    result = subtract(num1, num2)
elif choice == 3:
    result = multiply(num1, num2)
elif choice == 4:
    result = divide(num1, num2)

print("The result is", result)

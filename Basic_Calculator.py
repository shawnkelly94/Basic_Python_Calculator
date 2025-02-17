#This code will be for a very basic calculator that will add, subtract, multiply, and divide two numbers.
#The user will be prompted to enter two numbers and then choose an operation to perform on them.

operation = input("Enter an operator (+, -, *, /): ")
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
if operation == "+":
    print(number1 + number2)
    #Also could be written as sum(number1, number2)
elif operation == "-":
    print(number1 - number2)
    #Also could be written as difference(number1, number2)
elif operation == "*":
    print(number1 * number2)
    #Also could be written as product(number1, number2)
elif operation == "/":  
    if number2 == 0:
        print("You cannot divide by zero, silly.")
    else:
        print(number1 / number2)
    #Also could be written as quotient(number1, number2)
else:
    print(f"Invalid operator: {operation}")

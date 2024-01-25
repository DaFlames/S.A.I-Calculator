# Import the math module for mathematical operations
import math

# Prompt the user to input the first number
print("Enter input 1:")
Input_1 = int(input())

# Prompt the user to input the second number
print("Enter input 2:")
Input_2 = int(input())

# Display the available operations
print("a) Addition")
print("b) Subtraction")
print("c) Multiplication")
print("d) Division")

# Prompt the user to choose an operation
print("Choose Operation:")
Operation = input()

# Perform the selected operation and display the result
if Operation == 'a':
    result = Input_1 + Input_2
    print(f"{Input_1} + {Input_2} = {result}")
elif Operation == 'b':
    result = Input_1 - Input_2
    print(f"{Input_1} - {Input_2} = {result}")
elif Operation == 'c':
    result = Input_1 * Input_2
    print(f"{Input_1} * {Input_2} = {result}")
elif Operation == 'd':
    # Check for division by zero before performing the operation
    if Input_2 != 0:
        result = Input_1 / Input_2
        print(f"{Input_1} / {Input_2} = {result}")
    else:
        print("Error: Division by zero")
else:
    print("Invalid Operation")

# Allow the user to view the output before exiting
input("Press enter to exit")
# Import the math module for mathematical operations
import math

# Prompt the user to input the first number
print("Enter input 1:")
Input_1 = int(input())

# Prompt the user to input the second number
print("Enter input 2:")
Input_2 = int(input())

# Display the available operations
print("a) Addition")
print("b) Subtraction")
print("c) Multiplication")
print("d) Division")

# Prompt the user to choose an operation
print("Choose Operation:")
Operation = input()

# Perform the selected operation and display the result
if Operation == 'a':
    result = Input_1 + Input_2
    print(f"{Input_1} + {Input_2} = {result}")
elif Operation == 'b':
    result = Input_1 - Input_2
    print(f"{Input_1} - {Input_2} = {result}")
elif Operation == 'c':
    result = Input_1 * Input_2
    print(f"{Input_1} * {Input_2} = {result}")
elif Operation == 'd':
    # Check for division by zero before performing the operation
    if Input_2 != 0:
        result = Input_1 / Input_2
        print(f"{Input_1} / {Input_2} = {result}")
    else:
        print("Error: Division by zero")
else:
    print("Invalid Operation")

# Allow the user to view the output before exiting
input("Press enter to exit")

# Python Project 1 Simple Calculator
# Getting back in Python, simple algorithms

import os

programRun = True

while programRun:
    os.system('cls')
    print("Welcome to the calculator (2 numbers)")
    print("What would you want to do?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    userInput = int(input("Enter input: "))

    if userInput == 1:
        print("What is the first number?: ")
        firstNum = int(input("First number: "))
        
        print("What is the second number?: ")
        secondNum = int(input("Second number: "))
        
    if userInput == 2:
        print("What is the first number?: ")
        firstNum = int(input("First number: "))
        
        print("What is the second number?: ")
        secondNum = int(input("Second number: "))
        
    if userInput == 3:
        print("What is the first number?: ")
        firstNum = int(input("First number: "))
        
        print("What is the second number?: ")
        secondNum = int(input("Second number: "))
        
    if userInput == 4:
        print("What is the first number?: ")
        firstNum = int(input("First number: "))
        
        print("What is the second number?: ")
        secondNum = int(input("Second number: "))
        
    if userInput == 5:
        print("Goodbye")
        programRun = False
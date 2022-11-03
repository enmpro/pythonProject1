# Python Project 1 Simple Calculator
# Getting back in Python, simple algorithms

import os # import for clear screen
import mathFunc # import user module

programRun = True

while programRun: # make program run continuously
    os.system('cls')
    print("Welcome to the calculator (2 numbers)")
    print("What would you want to do?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    userInput = int(input("Enter input: "))

    if userInput == 1: # call function from module
        mathFunc.addFunction()
        
    if userInput == 2:
        mathFunc.subtractFunction()
        
    if userInput == 3:
        mathFunc.multiplyFunction()
        
    if userInput == 4:
        mathFunc.divideFunction()
        
    if userInput == 5:
        print("Goodbye")
        programRun = False
def addFunction(): 
    while True:
        print("What is the first number?: ")
        try: 
            firstNum = int(input("First number: "))
        except:
            print("\nEnter a valid number.\n")
            continue
        print("What is the second number?: ")
        try: 
            secondNum = int(input("Second number: "))
        except:
            print("\nEnter a valid number.\n")
            continue
        
        total = firstNum + secondNum
        print(f"Total: {total}")
        break
    
    
def subtractFunction(): 
    while True:
        print("What is the first number?: ")
        try: 
            firstNum = int(input("First number: "))
        except:
            print("\nEnter a valid number.\n")
            continue
        print("What is the second number?: ")
        try: 
            secondNum = int(input("Second number: "))
        except:
            print("\nEnter a valid number.\n")
            continue
        
        total = firstNum - secondNum
        print(f"Total: {total}")
        break
    
    
def multiplyFunction(): 
    while True:
        print("What is the first number?: ")
        try: 
            firstNum = int(input("First number: "))
        except:
            print("\nEnter a valid number.\n")
            continue
        print("What is the second number?: ")
        try: 
            secondNum = int(input("Second number: "))
        except:
            print("\nEnter a valid number.\n")
            continue
        
        total = firstNum * secondNum
        print(f"Total: {total}")
        break
    
    
def divideFunction(): 
    while True:
        print("What is the first number?: ")
        try: 
            firstNum = int(input("First number: "))
        except:
            print("\nEnter a valid number.\n")
            continue
        print("What is the second number?: ")
        try: 
            secondNum = int(input("Second number: "))
        except:
            print("\nEnter a valid number.\n")
            continue
        
        total = firstNum / secondNum
        print(f"Total: {total}")
        break
    

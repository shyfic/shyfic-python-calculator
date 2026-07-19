import functions

while True:
    x = float(input("Enter the value of X: "))
    print(f"Your X value is {x}")
    y = float(input("Enter the value of Y: "))
    print(f"Your Y value is {y}")
    choice = int(input("Enter the operation:\n(1) for addition\n(2) for subtraction\n"
    "(3) for multiplication\n(4) for division\n(5) for exponent\n(6) for root\n"))

    def operation(choice, x, y):
        match choice:
            case 1:
                return functions.addition(x, y)
            case 2:
                return functions.subtraction(x, y)
            case 3:
                return functions.multiplication(x, y)
            case 4:
                return functions.division(x, y)
            case 5:
                return functions.exponent(x, y)
            case 6:
                return functions.root(x, y)
            case _:
                print("Please input a correct option (1-6)")
                return None 

    result = operation(choice, x, y)
    if result is not None:
        print(f"The result is: {result}")
        looping_check = int(input(f"Press (1) to continue and (2) to exit"))
    if looping_check == 2:
        break    

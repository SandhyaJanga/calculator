while(True):    
    print("Simple Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    #codeSoft
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    choice = input("Select an operation (1/2/3/4): ")

    if choice == '1':
        print(n1, "+", n2, "=", n1 + n2)

    elif choice == '2':
        print(n1, "-", n2, "=", n1 - n2)

    elif choice == '3':
        print(n1, "×", n2, "=", n1 * n2)

    elif choice == '4':
        if n2 != 0:
            print(n1, "÷", n2, "=", n1 / n2)
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid input")
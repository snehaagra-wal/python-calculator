def simple_calculator():
    
    #prompt user fot two input numbers and select operation to perform calculation.
    print("Simple python Calculator")

    #get first number input using float to allow for both decimal and integer
    try:
        num1 = float(input("Enter the first number:"))
    except ValueError:
        print("❌Error: please enter a valid number for first input.")
        return

#select operation input

    operation = input("Enter operation +,-,*,/:").strip()

#get second number input
    try:
        num2 = float(input("Enter the second number:"))
    except ValueError:
        print("❌Error: please enter a valid number for second input.")
        return


    

    result = None

#perform calculation based on selected operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
    # Crucialcheck to prevent program from crashing 

        if num2 == 0: 
            print("❌Error: undefined")
            return
        else:
            result = num1 / num2
    else:
        print("Invalid operation")
        return

    #Display the result
    print("-" * 30)
    print("Result:", round(result, 2))
    print("-" * 30)

    #to execute using  call function
simple_calculator()

     




    


    
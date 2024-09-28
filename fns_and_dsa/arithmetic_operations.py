def perform_operation(num1,num2,operation):


    if "add":
        return num1+num2

    elif "subtract":
        return num1-num2

    elif "multiply":
        return num1*num2

    elif "divide":
        return num1/num2
        if num1 or num2 == 0:
            return ("Invalid Operation.Number cannot be divided by zero")
    

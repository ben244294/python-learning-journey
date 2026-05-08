while True : #loop forever unless something triggers the loop to terminate in this case once the computation is done or the user enters x
    compute = input("Please enter your computation (or x tp quit):")
    if compute == "x":
        break
    try:
        result = eval(compute)
        print(f"your result is {result}")
    except ZeroDivisionError: #error handling
        print("Error: you cannot divide by zero")
    except (ValueError, SyntaxError):
        print("Error:Invalid expression entered")


def input_numbers():
    number = int(input("Enter your number: "))
    if number < 0:
        print("Number -ve")
    else:
        print("Number +ve")
        input_numbers()  # Recursive call if the number is non-negative

# Start the program
input_numbers()
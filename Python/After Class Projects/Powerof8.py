def is_power_of_8(n):
    if n < 1:
        return False
    while n % 8 == 0:
        n /= 8
    return n == 1


try:
    number = int(input("Enter your number: "))
    if is_power_of_8(number):
        print(f"Yes {number} is a power of 8.")
    else:
        print(f"No {number} is not a power of 8.")
except ValueError:
    print("Please enter a valid integer.")
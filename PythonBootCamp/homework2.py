
# Problem 1: Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("This operation is not supported")
else:
    print(f"All went well")


# Problem 2: Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'
try:
    x = 5
    y = 0
    z = x / y
    print(z)
except ZeroDivisionError:
    print("Division by zero is not allowed")
finally:
    print("All Done.")


# Problem 3: Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    while True:
        try:
            begs = int(input("Please enter an integer: "))
        except ValueError:
            print("That's not an integer. Please ensure you enter an integer")
            continue
        else:
            print(f"Thank you for inputting {begs ** 2}")
            break

ask()
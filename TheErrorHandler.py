try:
    x = 1 / 0
except ZeroDivisionError:
    pass
#added colon at the end of the "expect"


try:
    # Division
    x = 1 / 0

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Invalid input. Please provide a valid number.")

# File Reading
try:
    filename = input("Enter the filename to read: ")
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)

except FileNotFoundError:
    print("File not found!")

except Exception as e:
    print("An error occurred:", str(e))

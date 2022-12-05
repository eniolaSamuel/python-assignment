positive_number = int(input("Enter a positive number:"))

while positive_number < 0:
    print("You are quite dense")
    positive_number = int(input("Enter a positive number:"))

print("You have entered", positive_number)

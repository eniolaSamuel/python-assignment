count = 0
largest = float("-inf")
smallest = float("inf")

attempt = bool(True or False)

while attempt:
    number = int(input("Input number or enter 0 to end: "))

    if number == '0':
        print("Thanks for your input")
        break

    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("The largest number is", largest)
print("The smallest number is", smallest)

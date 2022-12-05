count = 0
smallest_so_far = float("inf")
while count < 5:
    number = int(input("Give me a number: "))
    if number > smallest_so_far:
        smallest_so_far = number

    count += 1

print("The smallest number is", smallest_so_far)

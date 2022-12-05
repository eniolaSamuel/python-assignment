count = 0

largest_so_far = float("-inf")
second_largest_so_far = float("-inf")

while count < 5:
    number = int(input("Give me a number: "))

    if number > largest_so_far:
        second_largest_so_far = largest_so_far
        largest_so_far = number

    elif (number > second_largest_so_far) and (number < largest_so_far):
        second_largest_so_far = number

    count += 1

print("The largest number is", largest_so_far)
print("The second largest is", second_largest_so_far)

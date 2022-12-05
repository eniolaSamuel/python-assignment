number = int(input("Enter a number: "))
count = 1
sum_of_count = 0
while count < number:
    if number % count == 0:
        sum_of_count = sum_of_count + count
    print(number)

    count += 1
if sum_of_count == number:
    print(number, "is a perfect number")

if sum_of_count < number:
    print(number, "is a deficient number")

if sum_of_count > number:
    print(number, "is an abundant number")

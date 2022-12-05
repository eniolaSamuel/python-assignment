import random

count = 0

guess_number = random.randint(1, 100)

while count < 3:
    guess = int(input("Guess a number from 1 to 100: "))

    if guess == guess_number:
        print("You got that right")
        break

    if guess < guess_number:
        print("Input smaller than Number ")
    if guess > guess_number:
        print("Input larger than Number")
    count += 1
if count == 3:
    print("It is quite unfortunate you are wrong, number is:", guess_number)

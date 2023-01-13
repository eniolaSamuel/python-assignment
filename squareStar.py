def square_star():
    square = int(input("Enter square size: "))
    star = " *"
    space = " "

    print(star * square)
    for i in range(0, square):
        print(star, end="")
        print(space * (square-1), end="")
        print(star, end="")


square_star()


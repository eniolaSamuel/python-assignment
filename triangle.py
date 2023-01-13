def triangle_printing():
    user_input = int(input("Enter size of triangle: "))
    for i in range(0, user_input):
        for j in range(0, i + 1):
            print("*", end=" ")
        print()



triangle_printing()
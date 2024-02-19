def add_this(*numbers, **kwargs):
    sum = 0
    for x in numbers:
        sum += x
    print("Sum: " + str(sum))

add_this(2, 2, 3, 2, namn="hjalmar")


def average_numbers(n):
    sum = 0
    for i in range(0, n):
        x = input("Number:\n")
        sum += int(x)
    print("Average = {}".format(round(1.0 * sum / n, 2)))

cnt = 0
tot = 0
def average_numbers(x):
    global cnt
    global tot
    cnt = cnt + x
    tot = tot + 1
    return round((1.0 * cnt / tot), 2)

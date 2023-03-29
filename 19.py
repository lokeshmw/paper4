def func(n):
    for a in range(1, n + 1):
        if a % 5 == 0 and a % 2 == 0:
            yield a


for i in func(20):
    print(i)

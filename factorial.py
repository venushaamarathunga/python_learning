def factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

for n in range(1, 6):
    print(n, " --> ", factorial(n))
def fibonacci(n):
    if n <= 0:
        return None
    elif n < 3:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n -2)
    
for n in range(1, 11):
    print(n, " --> ", fibonacci(n))

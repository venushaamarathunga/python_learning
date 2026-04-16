def factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    
    product = 1
    for i in range(2, n+1):
        product *= i
    return product

for n in range(1, 6):
    print(n, " --> ", factorial(n))
def fibonacci(n):
    if n <= 0:
        return None
    elif n < 3:
        return 1
    
    elem1 = elem2 = 1
    sum = 0
    for i in range(3 , n+1):
        sum = elem1 + elem2 
        elem1, elem2 = elem2, sum
    return sum
    
for n in range(1, 11):
    print(n, " --> ", fibonacci(n))

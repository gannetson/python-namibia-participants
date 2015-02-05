def iter_factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

def recur_factorial(n):
    
    if n == 1:
        return 1

    return n * recur_factorial(n - 1)

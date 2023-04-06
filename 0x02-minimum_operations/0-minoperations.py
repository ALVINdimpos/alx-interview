def minOperations(n):
    if n <= 1:
        return 0
    i = 2
    res = n
    while i * i <= n:
        if n % i == 0:
            res = res - (res // i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        res = res - (res // n)
    return res
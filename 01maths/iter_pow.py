def iter_pow(x, n):
    res = 1
    while n > 0:
        if n%2 != 0:
            res = res*x
        x = x*x
        n = n//2
    return res


print(iter_pow(3, 4))
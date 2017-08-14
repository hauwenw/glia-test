
cache = {}
def combinatioOptimized(n,r):
    if (n,r) in cache:
        return cache[(n,r)]
    if(r == 1):
        result = cache[(n,r)] = n
    elif(n == r):
        result = cache[(n,r)] = 1
    else:
        result = cache[(n,r)] = combinatioOptimized(n-1,r) + combinatioOptimized(n-1,r-1)
    return result

print(combinatioOptimized(990,33))
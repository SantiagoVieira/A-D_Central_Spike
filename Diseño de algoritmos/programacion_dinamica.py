def factorialcache(num, cache = [], i = 0):
    if num == 0 or num == 1:
        cache.append(num)
        return num
    if len(cache)>=num:
        return cache[num-1]
    else:
        cache.append(num * factorialcache(num-1, cache))
        return cache[num-1]

print(factorialcache(10))

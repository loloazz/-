from functools import lru_cache


@lru_cache(None)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y



print(add(1, 2))
print(add(1,2))

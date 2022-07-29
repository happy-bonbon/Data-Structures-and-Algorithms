import math


def findnumber():
    '''not correct'''
    low, high = 1000000, 10000000
    while low <= high:
        mid = (low+high) // 2
        something = math.isqrt(mid)**2
        if something == mid:
            return mid
        elif something > mid:
            low = mid+1
        else:
            high = mid-1
    return "GG"


print(findnumber())

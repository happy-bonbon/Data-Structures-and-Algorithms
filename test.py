def find_outlier(integers):
    even = 0
    if integers[0] % 2 == 0:
        even += 1
    if integers[1] % 2 == 0:
        even += 1
    if integers[2] % 2 == 0:
        even += 1
    if even > 1:
        for item in integers:
            if item % 2 != 0:
                return item
    else:
        for item in integers:
            if item % 2 == 0:
                return item


print(find_outlier([2, 4, 6, 8, 10, 3]), 3)

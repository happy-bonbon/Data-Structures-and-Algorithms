def binary_tree(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


# def locate_card(card, target):

#     def condition(mid):
#         if card[mid] == target:
#             if mid > 0 and card[mid-1] == target:
#                 return 'left'
#             else:
#                 return 'found'
#         elif card[mid] > target:
#             return 'right'
#         else:
#             return 'left'

#     lo, hi = 0, len(card) - 1
#     return binary_tree(lo, hi, condition)

nums = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11]
numsc = nums[::-1]
target = 5
result = 4, 12


def locate_number(nums, target):

    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            else:
                return 'found'
        elif nums[mid] > target:
            return 'left'
        else:
            return 'right'

    return binary_tree(0, len(nums)-1, condition)


def locate_numberc(nums, target):

    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            else:
                return 'found'
        elif nums[mid] > target:
            return 'right'
        else:
            return 'left'

    return binary_tree(0, len(nums)-1, condition)


if locate_number(nums, target) == -1:
    print([-1, -1])
else:
    print([locate_number(nums, target), len(nums)-locate_numberc(numsc, target)-1])

# print(locate_number(nums, target))
# if result == (locate_number(nums, target), len(nums)-locate_numberc(numsc, target)-1):
#     print("Nice")
# else:
#     print("GG")

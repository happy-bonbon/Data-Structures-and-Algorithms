'''34. Find First and Last Position of Element in Sorted Array'''
""" Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1] 

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""


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


nums = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11]
# numsc = nums[::-1]
target = 5
result = 4, 12


def locate_first_number(nums, target):

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


def locate_last_number(nums, target):

    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            else:
                return 'found'
        elif nums[mid] > target:
            return 'left'
        else:
            return 'right'

    return binary_tree(0, len(nums)-1, condition)


print([locate_first_number(nums, target), locate_last_number(nums, target)])


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


# def locate_number(nums, target):

#     def condition(mid):
#         if nums[mid] == target:
#             if mid > 0 and nums[mid-1] == target:
#                 return 'left'
#             else:
#                 return 'found'
#         elif nums[mid] > target:
#             return 'left'
#         else:
#             return 'right'

#     return binary_tree(0, len(nums)-1, condition)


# def locate_numberc(nums, target):

#     def condition(mid):
#         if nums[mid] == target:
#             if mid > 0 and nums[mid-1] == target:
#                 return 'left'
#             else:
#                 return 'found'
#         elif nums[mid] > target:
#             return 'right'
#         else:
#             return 'left'

#     return binary_tree(0, len(nums)-1, condition)


# if locate_number(nums, target) == -1:
#     print([-1, -1])
# else:
#     print([locate_number(nums, target),
#            len(nums)-locate_numberc(numsc, target)-1])
# print(locate_number(nums, target))

# if result == (locate_number(nums, target),
#               len(nums)-locate_numberc(numsc, target)-1):
#     print("Nice")
# else:
#     print("GG")

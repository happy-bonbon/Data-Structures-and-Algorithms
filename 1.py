'''1. Two Sum'''
""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1] """


from colorama import Fore


def two_sum(nums, target):
    '''O(n)'''
    lst = list(enumerate(nums))
    for item in lst:
        complement = target - item[1]
        if complement in nums[item[0]+1:]:
            return [item[0], nums[item[0]+1:].index(complement)+item[0]+1]


# def two_sum(nums, target):
#     '''try to use dict, doesnt work'''
#     lst = dict(enumerate(nums))
#     lst = {v: k for k, v in lst.items()}
#     print(lst)


#     for item in lst:
#         complement = target - nums
#         index = lst[item]
#         indexx = lst[complement]
#         print(index, indexx)
#         if complement in lst and lst[complement] != index:
#             print([index, lst[complement]])
#             return [index, lst[complement]]


# def two_sum(nums, target):
#     '''from leetcode answer'''
#     hashmap = {}
#     for i in range(len(nums)):
#         hashmap[nums[i]] = i
#     for i in range(len(nums)):
#         complement = target - nums[i]
#         if complement in hashmap and hashmap[complement] != i:
#             return [i, hashmap[complement]] 


# def two_sum(nums, target):
#     '''from leetcode answer'''
#     hashmap = {}
#     for i in range(len(nums)):
#         complement = target - nums[i]
#         if complement in hashmap:
#             return [hashmap[complement], i]
#         hashmap[nums[i]] = i


tests = []
tests.append({
    'Case': 1, 'input': {
        'nums': [2, 7, 11, 15], 'target': 9},
    'output': [0, 1]})
tests.append({
    'Case': 2, 'input': {
        'nums': [3, 2, 4], 'target': 6},
    'output': [1, 2]})
tests.append({
    'Case': 3, 'input': {
        'nums': [3, 3], 'target': 6},
    'output': [0, 1]})


for test in tests:
    result = two_sum(**test['input'])
    if result == test['output']:
        print(Fore.BLUE + 'Case ' +
              str(test['Case']) + ':' + Fore.GREEN + ' PASS!')
    else:
        print(Fore.BLUE + 'Case ' +
              str(test['Case']) + ':' + Fore.RED + ' GG!')

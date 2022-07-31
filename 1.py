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

tests = []
tests.append({
    'Case': 1, 'input': {
        'nums': [2, 7, 11, 15], 'target': 9},
    'output': [0, 1]})
tests.append({
    'Case': 1, 'input': {
        'nums': [3, 2, 4], 'target': 6},
    'output': [1, 2]})
tests.append({
    'Case': 1, 'input': {
        'nums': [3, 3], 'target': 6},
    'output': [0, 1]})


def two_sum(nums, target):
    lst = list(enumerate(nums))
    for item in lst:
        other_half = target - item[1]
        if other_half in nums[item[0]+1:]:
            return [item[0], nums[item[0]+1:].index(other_half)+item[0]+1]


for test in tests:
    result = two_sum(**test['input'])
    if result == test['output']:
        print(Fore.BLUE + 'Case ' +
              str(test['Case']) + ':' + Fore.GREEN + ' PASS!')
    else:
        print(Fore.BLUE + 'Case ' +
              str(test['Case']) + ':' + Fore.RED + ' GG!')

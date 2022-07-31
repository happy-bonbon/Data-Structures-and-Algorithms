'''14. Longest Common Prefix'''
""" Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


strs = ["dog","racecar","car"]
strs = ["flower", "flow", "flight"]
strs = ["cir","car"]


def longestCommonPrefix(strs):
    '''assume the shortest word is the prefix, 
    return its characters one by one until it isn't'''
    sml = min(strs, key=len)
    common = ''
    
    for i in range(len(sml)):
        letter = sml[i]
        for item in strs:
            if letter != item[i]:
                letter = ''
                break
        else:
            common += letter
            continue
        break
    return common


print(longestCommonPrefix(strs))

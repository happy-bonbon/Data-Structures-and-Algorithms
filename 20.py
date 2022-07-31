'''20. Valid Parentheses'''
""" Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false 

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

s = "([)]"
s = "()"
s = "()[]{}"
s = "(]"
s = "{[()]}"
s = "["
s = "([]())[{()}]{}"


def isValid(s):
    '''look for the inner most close bracket, match it and then delete it, repeat'''
    hashmap = {')': '(', ']': '[', '}': '{'}

    while len(s) > 0:
        lst = []
        if ')' in s:
            lst.append(s.index(')'))
        if ']' in s:
            lst.append(s.index(']'))
        if '}' in s:
            lst.append(s.index('}'))
        if len(lst) > 0:
            index = min(lst)
            if index < 1 or hashmap[s[index]] != s[index-1]:
                return False
            else:
                s = s[:index-1]+s[index+1::]
        else:
            return False
    return True


print(isValid(s))

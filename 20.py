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


s = "{[()]}"
s = "([)]"
s = "(]"
s = "()"
s = "()[]{}"
s = "([]())[{()}]{}"


def isValid(s):

    hashmap = {'(': ')', '[': ']', '{': '}'}
    print(hashmap)

    if len(s) % 2 == 0:
        mid = int(len(s)/2)
        left = s[:mid]
        print(left)
        right = s[-1:mid-1:-1]
        print(right)

        for i in range(mid):
            print(hashmap[left[i]])
            if hashmap[left[i]] != right[i] and hashmap[left[i]] != s[i+1]:
                return False
        return True

        # strs=s[::2]
        # print(strs)
        # for i in range(len(strs)-1):
        #     print(i)
        #     print(s[i])
        #     if strs[i] == '(' and s[i+1] != ')':
        #         return False
        #     elif strs[i] == '[' and s[i+1] != ']':
        #         return False
        #     elif strs[i] == '{' and s[i+1] != '}':
        #         return False

            # if s[i] != ')' and s[i] != ']' and s[i] != '}':

            #     print('ok')
    else:
        return False


# def isValid(s):
#     a, b, c = 0, 0, 0
#     if len(s) % 2 == 0:
#         for item in s:
#             if item == '(':
#                 a += 1
#             elif item == '[':
#                 b += 1
#             elif item == '{':
#                 c += 1
#             elif item == ')':
#                 a -= 1
#             elif item == ']':
#                 b -= 1
#             elif item == '}':
#                 c -= 1
#         if a == b == c == 0:
#             return True
#         else:
#             return False
#     else:
#         return False

# isValid(s)
print(isValid(s))

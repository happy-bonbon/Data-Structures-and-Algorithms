'''9. Palindrome Number'''

""" Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome. """


# x=0
# x = 121
# x = 1234567
# x=100000001
x = 1234567890987654321


def isPalindrome(x):
    '''no string faster version'''
    number, orignal_number = 0, x
    if x >= 0:
        while x > 0:
            digit = x % 10
            number = number * 10 + digit
            x = x // 10
        return number == orignal_number
    else:
        return False


print(isPalindrome(x))


# def palindrome(x):
#     '''with string'''
#     return str(x) == str(x)[::-1]


# def palindrome(x):
#     '''with string, faster version'''
#     x = str(x)
#     return x == x[::-1]


# def isPalindrome(x):
#     '''no string'''
#     if x > 0:
#         n, y, z, number = math.floor(math.log10(x)+1), 0, 0, 0
#         while n > 0:
#             y = x % (10**n)//(10**(n-1))
#             n -= 1
#             number = number + y * 10**z
#             print(number)
#             z += 1
#         return number == x
#     elif x == 0:
#         return True
#     else:
#         return False

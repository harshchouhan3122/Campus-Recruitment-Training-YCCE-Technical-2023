'''
 Palindrome
Problem description:
Write a function to find if a given string is a palindrome or not. Return 0 if the input string is 
not a palindrome and 1 if the input string is a palindrome.
Note: A string is said to be a palindrome if the reverse of the string is the same as the string. 
For example, “abba” is a palindrome, but “abbc” is not a palindrome.
Input Specification:
input1: A string of characters
Output Specification:
0 or 1 depending on whether the string is a palindrome or not.
Example 1:
input1: level
Output: 1
Explanation:
The reverse of string “level” is “level”. As they are the same hence the string is a palindrome.
'''

def isPalindrome (org_string):
    rev_string = ""
    for i in range(len(org_string)):
        rev_string = org_string[i] + rev_string
    if rev_string == org_string :
        return True
    else:
        return False

org_string = input("Enter any String : ")
print(int(isPalindrome(org_string)))
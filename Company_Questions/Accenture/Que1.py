'''
Write a function to validate if the provided two strings are anagrams or not. If the
two strings are anagrams, then return ‘yes’. Otherwise, return ‘no’.
Input:
Input 1: 1st string
Input 2: 2nd string
Output:
(If they are anagrams, the function will return ‘yes’. Otherwise, it will return ‘no’.)
Example
Input 1: Listen
Input 2: Silent
Output:
Yes
Explanation
Listen and Silent are anagrams (an anagram is a word formed by rearranging the letters
of the other word)'''

def isAnagram(str1,str2):
    str1 = str(list(str1.lower()).sort())
    str2 = str(list(str2.lower()).sort())
    if str1 == str2:
        ans = "YES"
    else:
        ans = "NO"
    return ans

str1 = input("String 1 : ")
str2 = input("String 2 : ")

print(isAnagram(str1,str2))
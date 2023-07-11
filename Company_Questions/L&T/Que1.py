'''
 Fanny's Occurences
Fanny is given a string along with the string which contains a single character x. She has to 
remove the character x from the given string. Help her write a function to remove all 
occurrences of the x character from the given string
.
Input Specification:
input1: input string s
input2: String containing any character x
Output Specification:
String without the occurrence of character x
Example 1:
input1: welcome to metti
input2: i
Output: wecome to mett
Explanation: As I is the character that is required to be removed, therefore all the occurrences 
of I are removed, keeping all other characters
'''

string_1 = list(input("Enter String : "))
char_1 = input("Enter Character : ")

for i in string_1:
    if char_1==i:
        string_1.remove(i)

string_1 = "".join(string_1)

# string_1 = ''.join([char for char in string_1 if char != char_1])

print(string_1)
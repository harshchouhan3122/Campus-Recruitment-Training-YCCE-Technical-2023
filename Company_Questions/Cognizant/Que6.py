
'''
 Shambhu wants the magic board, which will display a character for the corresponding 
number in his science project. Now help him to develop such an application?
For Example: when the digits like 65, 66, 67, 68 are entered then the alphabet A B C and D will 
be displayed. Assume the no of inputs should be always 4

Sample Input 1:
Enter the digits:
65 66 67 68
Sample Output 1:
65-A 66-B 67-C 68-D

Sample Input 2:
Enter the digits:
115 116 101 112
Sample Output 2:
115-s 116-t 101-e 112-p

'''

numbers = list(map(int,input().split()))
# print(numbers)

# Conversion to character
for i in numbers:
    print("{}-{}".format(i,chr(i)),end=" ")



'''
You are required to implement the following function.
Int OperationChoices(int c, int a , int b )
The function accepts 3 positive integers ‘a’ , ‘b’ and ‘c ‘ as its arguments. Implement the 
function to return.
( a+ b ) , if c=1
( a – b ) , if c=2
( a * b ) , if c=3
(a / b) , if c =4
Assumption : All operations will result in integer output.
Example:
Input
c :1
a:12
b:16
Output:
Since ‘c’=1 , (12+16) is performed which is equal to 28 , hence 28 is returned.
Sample Input
c : 2
a : 16
b : 20
Sample Output
-4
'''

def OperationChoices(c,a,b):
    if c == 1:
        return(a+b)
    elif (c==2):
        return(a-b)
    elif (c==3):
        return(a*b)
    elif (c==4):
        return(a/b)

c = int(input("c : "))
a = int(input("a : "))
b = int(input("b : "))

print(OperationChoices(c,a,b))

# list1 = []
# for i in range(3):
#     list1.append(input().split(":"))

# for i in list1:
#     i[0] = int(i[1])

# print(list1)
# print("c : {}, a : {}, b : {}".format(c,a,b))

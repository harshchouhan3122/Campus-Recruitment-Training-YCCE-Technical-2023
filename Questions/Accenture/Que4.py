'''
Execute the given function.
def differenceofSum(n.m)
The function takes two integrals m and n as arguments. You are required to obtain the total of 
all integers ranging between 1 to n (both inclusive) which are not divisible by m.
You must also return the distinction between the sum of integers not divisible by m with the 
sum of integers divisible by m.
Example
Input:
m = 6
n = 30
Output:
285
Integers divisible by 6 are 6, 12, 18, 24, and 30. Their sum is 90.
Integers that are not divisible by 6 are 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 
20,
21, 22, 23, 25, 26, 27, 28, and 29. Their sum is 375.
The difference between them is 285 (375 – 90).
'''

def differenceOfSum(n,m):
    list1 = []
    list2 = []
    for i in range(1,n+1):
        if ( i%m == 0):
            list1.append(i)
        else:
            list2.append(i)
    sum1 = sum(list1)
    sum2 = sum(list2)

    diff = abs(sum1-sum2)

    return diff


n = int(input("Enter n : "))
m = int(input("Enter m : "))

print(differenceOfSum(n,m))

'''
Execute the given function:
LargeSmallSum(arr)
Input:
Arr: 3 2 1 7 5 4
Output:
8
Explanation
The largest element is 7.
The smallest element at is 1.
The output is 8 (7+1)
'''

def LargeSmallSum(arr):
    arr.sort()
    sum = int(arr[0])+int(arr[len(arr)-1])
    print("Sum : ",sum)

# Taking single line array input
arr = list(input("Enter Array : ").split(" "))
LargeSmallSum(arr)
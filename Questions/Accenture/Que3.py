'''
3. Solve the following
Productsmallpair(sum,arr)
Example
Input:
Sum: 9
Arr: 5 4 2 3 9 1 7
Output:
2
Explanation
From the array of integers, we have to select the two smallest numbers, i.e 2 and 1. 
Sum
of these two (2 + 1) = 3. This is less than 9 (3 < 9). The product of these two is 2 (2 x 1 =
2) Hence the output is integer 2.
Sample input:
Sum: 4
Arr: 9 8 –7 3 9 3
Sample output:
–21
'''

def ProductSmallPair(sum,arr):
    arr.sort()
    # arr = list(set(arr))
    ans = int(arr[0]) + int(arr[1])

    if ans < sum :
        print(int(arr[0]) * int(arr[1]))
    else:
        print(ans)


sum = int(input("Enter the Sum : "))
arr = list(input("Enter Array : ").split(" "))
# print(arr)
ProductSmallPair(sum,arr)

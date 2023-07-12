'''
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order. You don't need to read input or print anything. Your task is to complete the function sort012() that takes an array arr and N as input parameters and sorts the array in-place.

Input Format

5 0 2 1 2 0

Constraints

1 <= N <= 10^6 0 <= A[i] <= 2

Output Format

0 0 1 2 2

Sample Input 0

5
0 2 1 2 0
Sample Output 0

0 0 1 2 2
'''

def sort_array(array):
    count = len(array)
    while(count!=0):

        for i in range(len(array)):
            if i==len(array)-1:
                break

            j = i+1
            if array[i] > array[j]:
                temp = array[i]
                array.pop(i)
                array.insert(j,temp)

        count -= 1
    return array



# size = int(input())
array = list(map(int,input().split(" ")))
# print("Array : ",array)
print("Array : ",end="") 
for i in array:
    print(i,end=" ")  
print()

# Sorting an array directly using function
# array.sort()
# print(array)

# Sorting an array manually by writing new function
array = sort_array(array)
# print("Sorted Array : ",array)

print("Sorted Array : ",end="") 
for i in array:
    print(i,end=" ")    


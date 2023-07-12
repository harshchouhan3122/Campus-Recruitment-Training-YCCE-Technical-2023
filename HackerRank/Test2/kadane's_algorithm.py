# IMPORTANT QUESTION

'''
Given an array of N integers. Find the contiguous sub-array which has the maximum sum and return its sum.

Your Task: You don't need to read input or print anything. The task is to complete the function maxSubarraySum() which takes Arr[] and N as input parameters and returns the sum of subarray with maximum sum.

Example 1:

Input: N = 5 Arr[] = {1,2,3,-2,5}

Output: 9 Explanation: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.

Example 2:

Input: N = 4 Arr[] = {-1,-2,-3,-4}

Output: -1 Explanation: Max subarray sum is -1 of element (-1)

Input Format

N = 4 Arr[] = {-1,-2,-3,-4}

Constraints

1 ≤ N ≤ 106 -107 ≤ A[i] ≤ 107

Output Format

-1 Explanation: Max subarray sum is -1 of element (-1)

Sample Input 0

5
1,2,3,-2,5
Sample Output 0

9
'''

arr = list(map(int,input().split(",")))
sum,maxi=0,0

for i in range(len(arr)):
    # Kadane's Algorithm
    # Step1
    sum = sum + arr[i]
    # Step2
    maxi = max(maxi,sum)
    # Step3
    if sum<0:
        sum = 0

print(maxi)
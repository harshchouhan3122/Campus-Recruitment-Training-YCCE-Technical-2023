'''
Given an array A of positive integers. Your task is to find the leaders in the array. 
An element of array is leader if it is greater than or equal to all the elements to 
its right side. The rightmost element is always a leader.

Example 1:

Input: n = 6 A[] = {16,17,4,3,5,2}

Output: 17 5 2 Explanation: The first leader is 17 as it is greater than all the 
elements to its right. Similarly, the next leader is 5. The right most element 
is always a leader so it is also included.

Example 2:

Input: n = 5 A[] = {1,2,3,4,0}

Output: 4 0

Your Task: You don't need to read input or print anything. The task is to complete 
the function leader() which takes array A and n as input parameters and returns an 
array of leaders in order of their appearance.

Input Format

Input: n = 6 A[] = {16,17,4,3,5,2}

Constraints

1 <= n <= 107 0 <= Ai <= 107

Output Format

Output: 17 5 2 Explanation: The first leader is 17 as it is greater than all the 
elements to its right. Similarly, the next leader is 5. The right most element is 
always a leader so it is also included.

Sample Input 0

6
16 17 4 3 5 2
Sample Output 0

17 5 2
'''

# Function to find array leader
def array_leader(array):
    array_leader = []
    for i in range(len(array)):
        leader = array[i]

        for j in range(i+1,len(array)):
            if array[j] > leader:
                leader = array[j]
                if leader not in array_leader:
                    array_leader.append(leader)

        if i==len(array)-1:
            array_leader.append(array[-1])

    return array_leader


# Input
array = list(map(int,input().split()))

# Output
print(array_leader(array))

'''
Given two integers n and r, find nCr. Since the answer may be very large, calculate the answer modulo 109+7.

Example 1:

Input: n = 3, r = 2 Output: 3 Explaination: 3C2 = 3.

Example 2:

Input: n = 2, r = 4 Output: 0 Explaination: r is greater than n.

Your Task: You do not need to take input or print anything. Your task is to complete the function nCr() which takes n and r as input parameters and returns nCr modulo 109+7..

Input Format

3 2

Constraints

1 ≤ n ≤ 1000 1 ≤ r ≤ 800

Output Format

3

Sample Input 0

3
2
Sample Output 0

3
'''

# function for calculating factorial
def fact(num):
    if num==1 or num==0:
        return 1
    else:
        return num*fact(num-1)

# function for calculating nCr
# nCr = n! / r!*(n-r)!
def nCr(n,r):
    numerator = fact(n)
    denominator = fact(r)*fact(n-r)
    result = numerator/denominator
    return int(result)

# Input
n = int(input("n : "))
r = int(input("r : "))

# Output
print("nCr :",nCr(n,r))

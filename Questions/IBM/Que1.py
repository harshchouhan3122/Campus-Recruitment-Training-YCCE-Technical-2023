'''
Write a program to find HCF of two numbers by without using recursion.
Input format:
The first line contains any 2 positive numbers separated by space.
Output format:
Print the HCF of given two numbers.
Sample Input:
70 15
Sample Output:
5
'''

num1,num2 = input().split(" ")
num1,num2 = int(num1),int(num2)
# print("Value of num1 = {} and num2 = {}".format(num1,num2))

# Finding Factors of both the numbers
factorsNum1 = []
factorsNum2 = []
for i in range (1,num1+1):
    if num1%i==0:
        factorsNum1.append(i)
for i in range (1,num2+1):
    if num2%i==0:
        factorsNum2.append(i)
# print(factorsNum1)
# print(factorsNum2)

# Finding GCD or HCF
commonFactors=[]
if len(factorsNum1)>=len(factorsNum2):
    for i in factorsNum1:
        if i in factorsNum2:
            commonFactors.append(i)
else :
    for i in factorsNum2:
        if i in factorsNum1:
            commonFactors.append(i)

# print(commonFactors)
hcf = commonFactors[-1]
# print("HCF of {} and {} is {}.".format(num1,num2,hcf))
print(hcf)

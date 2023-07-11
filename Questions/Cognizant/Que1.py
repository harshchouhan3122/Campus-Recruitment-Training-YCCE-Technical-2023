# (IMPORTANT LCM- Unsolved)
'''
Find the LCM of Two given numbers?
In this question you have to accept two numbers from the user for which you have to find the 
LCM of the given numbers. The LCM stands for Lowest Common Factor which is the 
smallest number that divides both the given numbers.
Sample Input 1:
5 10
Sample Output 1:
10
Sample Input 2:
20 60
Sample Output 2:
60
'''

num1,num2 = input().split(" ")
num1,num2 = int(num1),int(num2)

min_num = min(num1,num2)
max_num = max(num1,num2)

condition = True
i=0
while (condition):
    i += 1
    if (min_num*i)%max_num==0:
        lcm = min_num*i
        condition = False
print(lcm)


'''
factors_num1 = []
factors_num2 = []

for i in range(1,num1+1):
    if num1%i==0 :
        factors_num1.append(i)
for i in range(1,num2+1):
    if num2%i==0 :
        factors_num2.append(i)

print(factors_num1)
print(factors_num2)
'''
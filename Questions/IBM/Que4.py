'''
Given a number x, determine whether the given number is Armstrong Number or not.
153 = 1+125+27 = 153
'''
num = int(input())
org_num = num
sum = 0
pow = len(str(num))
while(num!=0):
    sum += (num%10)**pow
    num //= 10
if sum == org_num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

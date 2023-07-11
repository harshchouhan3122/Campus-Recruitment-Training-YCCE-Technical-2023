'''
Program to check if a given number is a strong number or not is discussed here. A strong 
number is a number in which the sum of the factorial of the digits is equal to the number 
itself.
123 = 1! + 2! + 3! = 1 + 2 + 6 = 9  wrong
145 = 1! + 4! + 5! = 1 + 24 + 120 = 145
'''

def fact(num):
    if num == 0  or num ==1:
        return 1
    else:
        return num*fact(num-1)

num = int(input("Enter any Number : "))
org_num = num
sum = 0

while(num!=0):
    digit = num%10
    sum += fact(digit)
    num//=10

if sum == org_num:
    print("Strong Number")
else:
    print("Not a Strong Number")
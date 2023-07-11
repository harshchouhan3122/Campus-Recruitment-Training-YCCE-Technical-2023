'''
The program to check whether the given number is a palindrome or not. Any number is said 
to be a palindrome if the original number and the reverse of the original number are the same.
For example, 1234321 is a palindrome.
Original number = 1234321
The reverse of the number = 1234321
'''


org_num = int(input("Enter any number : "))
num = org_num
rev_num = 0
while(num!=0):
    digit = num%10
    rev_num = rev_num*10 + digit 
    num //= 10
if rev_num == org_num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


# Using reverse function
'''
org_num = int(input("Enter any number : "))
num = list(str(org_num))
num.reverse()
rev_num = int("".join(num))
# print(rev_num)
if org_num==rev_num:
    print("Palindrome Number")
else : 
    print("Not a Palindrome Number")
'''

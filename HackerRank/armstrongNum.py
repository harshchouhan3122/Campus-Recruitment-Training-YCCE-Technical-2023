orgnum = int(input())
num = orgnum
pow = len(str(num))
sum = 0

while(num!=0):
    digit = num%10
    sum = sum + digit**pow
    num //= 10

if orgnum == sum:
    print(sum)
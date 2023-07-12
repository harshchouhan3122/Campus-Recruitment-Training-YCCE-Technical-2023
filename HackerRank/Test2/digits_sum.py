'''
The modulo operator, %, returns the remainder of a division. For example, 4 % 3 = 1 and 12 % 10 = 2. The ordinary division operator, /, returns a truncated integer value when performed on integers. For example, 5 / 3 = 1. To get the last digit of a number in base 10, use as the modulo divisor.

Input Format

The input contains a single five digit number, .

Constraints

10000<=n<=99999

Output Format

Print the sum of the digits of the five digit number.

Sample Input 0

10564
Sample Output 0

16'''

num = int(input())

if num <= 99999 and num >= 10000:
    digits_sum = 0

    while(num!=0):
        digit = num % 10
        digits_sum += digit
        num //= 10

    print(digits_sum)

else:
    print("10000<=number<=99999")
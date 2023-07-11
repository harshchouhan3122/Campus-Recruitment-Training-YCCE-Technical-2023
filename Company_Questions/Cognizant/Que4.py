'''
Sanjana teaches her daughter how to find the factors of a given number. But when She 
provides a number to her daughter then the daughter should tell all the factors of that 
number correctly. So help Sanjana’s daughter by writing a program?
Note: If the entered input is zero then the output should be “No Factors”. And if the entered 
input is a negative number then first convert it to positive and then find its factors.

Sample Input 1:
Enter the positive integer: 55
Sample Output 1:
Factors of 55 are: 1 5 11 55

Sample Input 2:
Enter the positive integer-256
Sample Output 2:
Factors of 256 are: 1 2 4 8 16 32 64 128 256
'''

num = int(input())

if num == 0:
    print("No Factors")

else:
    if num < 0:
        num = abs(num)
    factors = []
    for i in range(1,num+1):
        if num%i==0:
            factors.append(i)
    # print(factors)
    print("Factors of {} are : ".format(num),end=" ")
    for i in factors:
        print(i,end=" ")

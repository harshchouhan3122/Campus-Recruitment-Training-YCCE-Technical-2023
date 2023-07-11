
'''
Write a program to print the prime number series from 1 to N where N is an input?
Sample Input 1:
15
Sample Output 1:
2 3 5 7 11 13
Sample Input 2:
5
Sample Output 2:
2 3 5
'''

num = int(input())

prime_numbers = []

for i in range(2,num+1):
    prime = True
    for j in range(2,i):
        if i%j==0:
            prime = False
            break
    if prime == True:
        prime_numbers.append(i)

# print(prime_numbers)
for i in prime_numbers:
    print(i,end=" ")
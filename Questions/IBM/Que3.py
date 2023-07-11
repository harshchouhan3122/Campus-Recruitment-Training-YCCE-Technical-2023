'''
Program to generate Fibonacci Triangle
1,1,2,3,5,8,13,21,......
'''

# First we will generate Fibonacci Series 
n = int(input("Enter No. of Rows : "))

total_terms = 0
for i in range(1,n+1):
    total_terms += int(i)
# print("total terms : ",total_terms)

fibonacci_series = [1,1]
a = 1
b = 1

for i in range(total_terms-2):
    c = a+b
    fibonacci_series.append(c) 
    a = b
    b = c

# print("Fibonacci Series : ",fibonacci_series)

# Printing Fibonacci Triangle
idx = 0
for i in range(1,n+1):
    for j in range(i):
        print(fibonacci_series[idx],end=" ")
        idx += 1
    print()


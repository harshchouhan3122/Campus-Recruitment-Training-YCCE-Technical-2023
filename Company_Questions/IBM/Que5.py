'''
Given a number n, print n-th Fibonacci number
'''

n = int(input("n : "))

# Print the Fibonacci series First
fibonacci_series = [1,1]
a = 1
b = 1
for i in range(n-2):
    c = a+b
    fibonacci_series.append(c)
    a = b
    b = c
# print(fibonacci_series)
print(fibonacci_series[-1])

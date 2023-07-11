# def factorial(num):
#     if (num==1 or num==0):
#         return 1
#     else:
#         fact = 1
#         for i in range(1,num+1):
#             fact *= i
#         return fact

# num = int(input())
# print(factorial(num))

# Using Recusrsion
def fact(num):
    if num < 0:
        return(-1)
    elif (num ==0 or num==1):
        return 1
    else:
        return num*fact(num-1)

num = int(input())
print(fact(num))
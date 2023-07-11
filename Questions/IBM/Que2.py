'''
Write a Program to Change Decimal Number to Binary?
'''
# # Using default function : bin()
# def Binary(decimal_num):
#     binary_num = bin(decimal_num)[2:]
#     return binary_num

def Binary(decimal_num):
    binary_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2
    if binary_num =="":
        binary_num = 0
    return binary_num

num = int(input("Decimal Number : "))
print("Binary Number : {}".format(Binary(num)))

# With Proper Explanation of Function
"""
binary_num = ""
decimal_num = int(input("Decimal : "))

while decimal_num > 0:
    print("Decimal : ",decimal_num)

    remainder = decimal_num % 2
    print("Remainder : ",remainder)

    print("BinaryNum : ",binary_num)
    binary_num = str(remainder) + binary_num
    print("BinaryNum : ",binary_num)

    decimal_num //= 2
    print("Decimal : ",decimal_num)

    print("---------------------")

if binary_num =="":
    binary_num = 0

print("Binary : ",binary_num)
""" 

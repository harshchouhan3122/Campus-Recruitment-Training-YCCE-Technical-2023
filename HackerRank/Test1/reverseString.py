str1 = input()
str2 = ""

# for i in range(len(str1)-1,-1,-1):
#     str2 += str1[i]
# print(str2)

count = 0
for i in str1:
    count += 1

for i in range(count-1,-1,-1):
    str2 += str1[i]
print(str2)
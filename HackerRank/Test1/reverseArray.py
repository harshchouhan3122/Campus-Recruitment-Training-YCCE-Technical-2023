# arr = list(map(int,input().split(" ")))
# size = arr[0]
# arr.remove(arr[0])

# print(arr)
# if size==len(arr):
#     revArr = []
#     for i in arr:
#         revArr.insert(0,i)
#     print(revArr)

# else:
#     print("NA")

arr = []
size = int(input())
for i in range(size):
    arr.append(input())
# print(arr)

revArr = []
for i in arr:
    revArr.insert(0,i)

for i in revArr:
    print(i)

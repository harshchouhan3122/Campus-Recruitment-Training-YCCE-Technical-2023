# def mergeArray(nums1,m,nums2,n):
    # nums = nums1[:m]+nums2[0:n]
    # nums.sort()
    # return nums

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

# print(mergeArray(nums1,m,nums2,n))

for i in range(len(nums1)-1):
    if nums1[i] == 0:
        nums1.remove(nums1[i])
print(nums1)
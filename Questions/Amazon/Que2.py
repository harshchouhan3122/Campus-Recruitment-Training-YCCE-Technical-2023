'''
Next larger element
Example 1:
Input: 
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element 
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? 
since it doesn't exist, it is -1.
'''

size = int(input("Size of Array : "))
arr = list(map(int,input("Array Elemnets : ").split(" ")))
# print(arr)

if size != len(arr):
    print("Enter {} elements in the array.".format(size))

new_arr = []
for i in range(0,len(arr)):

    if i == len(arr)-1:
        new_arr.append(-1)
        break

    element = arr[i]
    for j in range(i+1,len(arr)):
        if arr[j] > element:
            new_arr.append(arr[j])
            # element = arr[j]
            break

# print(new_arr)
print("Output : ",end="")
for i in new_arr:
    print(i,end=" ")
        
        





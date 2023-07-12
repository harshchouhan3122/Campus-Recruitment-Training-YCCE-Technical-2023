'''
You are given  triangles, specifically, their sides ,  and . Print them in the same style but sorted by their 
areas from the smallest one to the largest one. It is guaranteed that all the areas are different.

The best way to calculate a area of a triangle with sides ,  and  is Heron's formula:
        s = (a+b+c)/2       area(triangle) = (s(s-a)(s-b)(s-c))**(1/2)

Input Format

The first line of each test file contains a single integer .  lines follow with three space-separated integers, ,  and .

Constraints

, and 
Output Format

Print exactly  lines. On each line print  space-separated integers, the ,  and  of the corresponding triangle.

Sample Input 0

3
7 24 25
5 12 13
3 4 5
Sample Output 0

3 4 5
5 12 13
7 24 25
Explanation 0

The square of the first triangle is . The square of the second triangle is . The square of the third triangle is . So the sorted order is the reverse one.
'''

# Function to Calculate Area of the triangle using Heron's Formula
def area(a,b,c):
    # Semi perimeter of the triangle
    s = (a+b+c)/2
    # Calculate Area
    result = pow((s*(s-a)*(s-b)*(s-c)),0.5)

    return result


# Taking Input
num = int(input())
triangles = []
for i in range(num):
    temp_list = list(map(int,input().split(" ")))
    triangles.append(temp_list)
# print(triangles)

# Update the list by adding the calculated area of the triangle
for i in range(len(triangles)):
    triangles[i].append(area(triangles[i][0],triangles[i][1],triangles[i][2]))
triangles.sort(key=lambda x:x[3])
# print(triangles)

print()
# Output
for i in triangles:
    for j in range(len(i)-1):
        print(i[j],end=" ")
    print()























'''
# Using Dictionary
triangles_area = []

for i in range(len(triangles)):
    triangles_area.append(area(triangles[i][0],triangles[i][1],triangles[i][2]))
print(triangles_area)

dict1 = dict(zip(triangles_area,triangles))
sorted(dict1.keys)
print(dict1)
'''

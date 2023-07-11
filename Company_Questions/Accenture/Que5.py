'''
You are required to write the code. You can click on compile & run anytime to check the 
compilation/ execution status of the program. The submitted code should be 
logically/syntactically correct and pass all the test cases.
Ques: The program is supposed to calculate the distance between three points.
For
x1 = 1 y1 = 1
x2 = 2 y2 = 4
x3 = 3 y3 = 6
Distance is calculated as : sqrt(x2-x1)2 + (y2-y1)2
'''

x1,y1 = map(int,input("Enter Point1 : ").split(","))
x2,y2 = map(int,input("Enter Point2 : ").split(","))
dist1 = (((x2-x1)**2)+ (y2-y1)**2)**(1/2)
# print("The Distance between ({},{}) and ({},{}) is {}.".format(x1,y1,x2,y2,dist1))
print("The Distance between ({},{}) and ({},{}) is {} units.".format(x1,y1,x2,y2,round(dist1,2)))
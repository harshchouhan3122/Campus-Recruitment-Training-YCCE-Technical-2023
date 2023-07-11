'''
1. Problem Statement – Raj wants to know the maximum marks scored by him in each semester. 
The mark should be between 0 to 100, if it goes beyond the range display “You have entered 
invalid mark.”
Sample Input 1:
● Enter no of semester:
3
● Enter no of subjects in 1 semester:
3
● Enter no of subjects in 2 semester:
4
● Enter no of subjects in 3 semester:
2
● Marks obtained in semester 1:
50
60
70
● Marks obtained in semester 2:
90
98
76
67
● Marks obtained in semester 3:
89
76
Sample Output 1:
● Maximum mark in 1 semester:70
● Maximum mark in 2 semester:98
● Maximum mark in 3 semester:89
'''

numSem = int(input("Enter Number of Semesters : "))

# List containing number of semesters
semSub = []
for i in range(numSem):
    numSub = int(input("Enter the Number of Subjects in {} Semester : ".format(i+1)))
    semSub.append(numSub)
# print(semSub)

# Nested list of marks accoring to the semester
marks=[]
for i in semSub:
    tempList=[]
    for j in range(int(i)):
        mark = float(input("Enter marks of {} Semesters : ".format(semSub.index(i)+1)))
        tempList.append(mark)
    marks.append(tempList)
# print(marks)

# List of max marks obtained in semesters
maxMarks = []
for i in marks:
    i.sort()
    max = i[-1]
    maxMarks.append(max)
# print(maxMarks)

for i in range(len(maxMarks)):
    print("Max mark in {} semester : {}.".format((i+1),maxMarks[i]))

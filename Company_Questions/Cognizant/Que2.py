
'''
Shraddha Kapoor’s professor suggested her study hard and prepare well for the lesson on 
seasons. If her professor says month then, she has to tell the name of the season 
corresponding to that month. So write the program to get the solution to the above task?
 March to May – Spring Season
 June to August – Summer Season
 September to November – Autumn Season
 December to February – Winter Season

Note: The entered month should be in the range of 1 to 12. If the user enters a month less 
than 1 or greater than 12 then the message “Invalid Month Entered” should get displayed.
Sample Input 1:
Enter month: 6
Sample Output 1:
Season: Summer
Sample Input 2:
Enter month: 15
Sample Output 2:
Invalid Month Entered

'''

month = int(input())

if month>12 or month<1:
    print("Invalid Month Entered")
else:
    if month>=3 and month <=5:
        season ="Spring"
    elif month >=6 and month <=8:
        season ="Summer"
    elif month >=9 and month <=11:
        season ="Autumn"
    elif month ==12 or (month >= 1 and month <=2):
        season ="Winter"

    print("Season : {}".format(season))
    
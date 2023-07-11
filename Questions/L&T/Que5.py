'''
WAP to accept Cost Price from user and ask whether the user is a student or not. If
the user is student and cost price is greater than 500, give discount of 10% ELSE
discount will be 5%. If user is not student and cost price is greater 500 then give
discount of 8% ELSE discount will be 2%. (Take all inputs from USER
'''

cost_price = float(input("Cost Price : "))
user = int(input("Are you a Student? (Press 1 or 2) \n  1.Yes \t 2.No \nChoice : "))

if user == 1:
    user = "student"
else:
    user = "other"

if user == "student" : 
    if cost_price > 500 :
        amount = 0.90*cost_price
    else :
        amount = 0.95*cost_price
else:
    if cost_price > 500 :
        amount = 0.92*cost_price
    else :
        amount = 0.98*cost_price

print("Total Amount : Rs.{}".format(amount))

'''
Mayuri buys “N” no of products from a shop. The shop offers a different percentage of 
discount on each item. She wants to know the item that has the minimum discount offer, so 
that she can avoid buying that and save money.
[Input Format: The first input refers to the no of items; the second input is the item name, price 
and discount percentage separated by comma(,)]
Assume the minimum discount offer is in the form of Integer.
Note: There can be more than one product with a minimum discount.
Sample Input 1:
 4
mobile,10000,20
shoe,5000,10
watch,6000,15
laptop,35000,5
Explanation: The discount on the mobile is 2000, the discount on the shoe is
500, the discount on the watch is 900 and the discount on the laptop is 1750.
So the discount on the shoe is the minimum.
'''


# numItems = int(input("Enter the num of Items : "))
numItems = int(input())
Items = []
# Creating the list containg sub list of items with their details
for i in range(numItems):
    tempList = list(map(str,input().split(",")))
    Items.append(tempList)
# print(Items)

# Updating SubList with their Item Discounts
for i in Items:
    discountAmt = int(i[2])*(int(i[1]))/100
    i.append(discountAmt) 

# Creating another List of Item and Their DiscountedAmount
items = []
disc = []
for i in Items:
    items.append(i[0])
    disc.append(i[3])

# Minimum Discount in discList
minDisc = min(disc)
# Finding Index of MinDiscount
idx = disc.index(minDisc)
# Find the Item of that index
item = items[idx]

# print("{} has a minimum discount of {}.".format(item,minDisc))
print("\nThe discount on the {} is minimum with amount of Rs.{}".format(item,minDisc))

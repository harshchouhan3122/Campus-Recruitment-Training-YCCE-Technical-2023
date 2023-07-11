
'''
Darshan went to a movie with his fellow friends in a nearby theatre and during the half break, 
he purchased some pizzas, puffs, and cold drinks. Now consider the given prices:
 100 Rs / Pizza
 20 Rs / Puffs
 10 Rs / Cold drink
Write a program to generate the final bill so that darshan can pay?

Sample Input 1:
Enter the number of pizzas purchased: 10
The number of puffs purchased: 12
Enter the no of Cold Drinks purchased: 5
Sample Output 1:
Bill Details:
No of Pizzas: 10
The No of Puffs: 12
No of Cold drinks: 5
Total Price=1290

'''

coldDrink = int(input("Enter the No. of Cold Drinks purchased : "))
pizza = int(input("Enter the No. of Pizzas purchased : "))
puff = int(input("Enter the No. of Puffs purchased : "))

bill_amount = pizza*100 + puff*20 + coldDrink*10

print("No. of Pizzas : {}",pizza)
print("No. of Puffs : {}",puff)
print("No. of Cold Drinks : {}",coldDrink)
print("Total Price = ",bill_amount)


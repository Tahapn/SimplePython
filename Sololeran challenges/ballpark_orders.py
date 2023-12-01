#### problem ####
# You and three friends go to a baseball game and you offer to go to the concession stand for everyone.
# They each order one thing, and you do as well. Nachos and Pizza both cost $6.00. A Cheeseburger meal costs $10. Water is $4.00 and Coke is $5.00. Tax is 7%. 
 
# Task  
# Determine the total cost of ordering four items from the concession stand. If one of your friend’s orders something that isn't on the menu,
# you will order a Coke for them instead. 
 
# Input Format 
# You are given a string of the four items that you've been asked to order that are separated by spaces. 
 
# Output Format  
# You will output a number of the total cost of the food and drinks. 
 
# Sample Input  
# 'Pizza Cheeseburger Water Popcorn' 
 
# Sample Output  
# 26.75


#### solution #### 
foods = input()
price = {"Water":4,"Coke":5,"Cheeseburger":10,"Nachos":6,"Pizza":6}
foods = foods.split(" ")
total = 0
for food in foods :

    # if the food is not in the dictionary it will return 5 because that's the price of Coke.
    # we are suposed to buy them coke if they  order something that's not in the menu

    total += price.get(food,5)
    
print(total  + total * 0.07)
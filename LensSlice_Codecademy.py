#Creating a list of toppings and a list of prices
toppings = ["Pepperoni", "Pineapple", "Cheese", "Sausage", "Olives", "Anchovies", "Mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#Counting occurence of 2 in prices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#Finding length of toppings list
num_pizzas = len(toppings)

#Printing string
print("We sell", num_pizzas, "different kinds of pizza!")

#Creating 2D table combining Toppings and Prices
pizza_and_prices = [[2, "Pepperoni"], [6, "Pineapple"], [1, "Cheese"], [3, "Sausage"], [2, "Olives"], [7, "Anchovies"], [2, "Mushrooms"]]
print(pizza_and_prices)
#Sorting pizza_and_prices in increasing cost
pizza_and_prices.sort()
#Storing cheapest pizza
cheapest_pizza = pizza_and_prices[0]
#Storing most expensive
priciest_pizza = pizza_and_prices[-1]
#Removing most expensive after selling out
pizza_and_prices.pop()
#Adding new topping; Peppers, 2.5
pizza_and_prices.insert(4, [2.5, "Peppers"])
#Slicing list for cheapest pizza for mice
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
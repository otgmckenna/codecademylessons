#Provided code
from hashlib import new


hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Original Code
#Determining total price of cuts
total_price = 0
for price in prices:
    total_price += price

#Determining average cost
average_price = total_price/len(prices)
print("Average Haircut Price: ", round(average_price, 2))

#Reducing prices by $5
new_prices = [price - 5 for price in prices]
print(new_prices)

#Calculating total revenue
total_revenue = 0 #Initializing total_revenue at 0
for i in range(len(hairstyles)):
    total_revenue += prices[i]          #Adding prices at position i to total_revenue
    total_revenue += last_week[i]       #Adding number of purchases at position i to total_revenue
print("Total Revenue:", total_revenue)

#Calculating average daily revenue
average_daily_revenue = total_revenue/7
print("Average Daily Revenue:", round(average_daily_revenue, 2))

#Creating a list advertising all haircuts under $30
cuts_under_30 = [
    hairstyles[i]
    for i in range(len(hairstyles))
    if new_prices[i] < 30
]
print(cuts_under_30)
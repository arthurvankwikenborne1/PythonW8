drinks = {"Jupiler", "Duvel", "White Wine", "Red Wine", "Spa Sparkling", 
          "Spa Non-Sparkling", "Coca-Cola", "Fruit Juice"}

# Define the orders
order1 = ["Jupiler", "White Wine", "Jupiler", "Duvel", "Duvel"]
order2 = ["Jupiler", "Jupiler", "Duvel", "Lemonade", "White Wine", "Ice Tea", "Coca-Cola"]

def AllAreDrinksOnDrinkCard(order):
	setOrder = set(order)
	print(setOrder)
	if(setOrder.issubset(drinks)):
		print("Order Coming...")
	else:
		print("Not coming...")

AllAreDrinksOnDrinkCard(order1)
AllAreDrinksOnDrinkCard(order2)
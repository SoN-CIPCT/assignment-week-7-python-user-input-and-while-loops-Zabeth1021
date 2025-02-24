# Create an empty list for pizza orders
pizza_orders = []

# While loop to collect orders from user input
while True:
    # first question
    new_order = input("Would you like to enter a new order (y/n)? ")
   
    # If answer is Y = Yes run the loop
    if new_order.lower() == 'y':
        pizza_name = input("Enter the pizza name: ")
        pizza_orders.append(pizza_name)
    # else if answer is N = No exit the loop
    elif new_order.lower() == 'n':
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# empty list for finished pizzas
finished_pizzas = []

# Loop to say ordered pizzas are finished and move to finished list
for pizza in pizza_orders:
    print(f"Your {pizza} pizza pie is finished!")
   
    finished_pizzas.append(pizza)

# loop act as completion confirmation
for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")

# Additional actions to audit the two lists values, the items counts and a differential output that should always rqual 0 at the end of the day
print("\nPizza Orders List:", pizza_orders)
print("Finished Pizzas List:", finished_pizzas)
print("\nTotal number of items in Pizza Orders List:", len(pizza_orders))
print("Total number of items in Finished Pizzas List:", len(finished_pizzas))
outstanding_orders = len(pizza_orders) - len(finished_pizzas)
print("Outstanding Orders:", outstanding_orders)
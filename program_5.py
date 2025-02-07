# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
# Prices for each item
Hot_dog = 3.50
Chili_dog = 4.50
cheese = 0.50
peppers = 0.75
grilled_onions = 1.00
TAX_RATE = 0.07  # 7% tax

def order_hotdog():
    # Display the menu
    menu = (
        "Hot Dog: $3.50\n"
        "Chili Dog: $4.50\n"
        "Cheese: $0.50\n"
        "Peppers: $0.75\n"
        "Grilled Onions: $1.00"
    )
    print(menu)

    # Get the user's hot dog choice
    hotdog_choice = input("What kind of hot dog would you like? (Hot Dog / Chili Dog): ")

    # Initialize base price and toppings string
    total_cost = 0
    topping_details = ""  # String to store selected toppings

    # Determine hot dog price based on user's choice
    if hotdog_choice.lower() == "hot dog":
        total_cost += Hot_dog
        topping_details = "Hot Dog"
    elif hotdog_choice.lower() == "chili dog":
        total_cost += Chili_dog
        topping_details = "Chili Dog"
    else:
        print("Sorry, we don't have that on the menu.")
        return None, None, None, None  # Return None if invalid choice

    # Ask about optional toppings
    cheese_choice = input("Would you like cheese? (yes/no): ").lower()
    if cheese_choice == "yes":
        total_cost += cheese
        topping_details += ", Cheese"

    peppers_choice = input("Would you like peppers? (yes/no): ").lower()
    if peppers_choice == "yes":
        total_cost += peppers
        topping_details += ", Peppers"

    onions_choice = input("Would you like grilled onions? (yes/no): ").lower()
    if onions_choice == "yes":
        total_cost += grilled_onions
        topping_details += ", Grilled Onions"

    # Calculate tax
    tax = total_cost * TAX_RATE
    total_with_tax = total_cost + tax

    return topping_details, total_cost, tax, total_with_tax


# Main execution
topping_details, total_cost, tax, total_with_tax = order_hotdog()

if topping_details:
    print("\n---Order Summary---")
    print(f"Hot Dog Choice: {topping_details}")
    print(f"Cost of Hot Dog: ${total_cost:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total Cost: ${total_with_tax:.2f}")

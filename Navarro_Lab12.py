# paglagay ng menu
def display_menu():
    print("Good day! Welcome to our Restaurant!")
    print("Here is our menu:")
    menu = {
        "Chickenjoy": 99.00,
        "CheeseBurger": 75.00,
        "Spaghetti": 72.00,
        "Mcfloat": 60.00,
        "Coke": 50.00
    }
    
    for item, price in menu.items():
        print(f"{item}: ₱{price:.2f}")
        
    return menu

# sa pag process ng order
def take_order(menu):
    while True:
        order_item = input("\nPlease enter the food item you want to order (or type 'exit' to quit): ").capitalize()
        
        if order_item.lower() == 'exit':
            print("Thank you for visiting, we're hoping to see you again!")
            return None, 0  # User wants to exit, return None and zero
        
        if order_item in menu:
            quantity = int(input(f"How many {order_item}s would you like to order? "))
            total_cost = menu[order_item] * quantity
            print(f"Your order: {quantity} {order_item}(s) - Total: ₱{total_cost:.2f}")
            return order_item, total_cost
        else:
            print("Invalid item. Please choose from the menu.")

# pag process ng payment
def process_payment(total_cost):
    while True:
        cash_rendered = float(input(f"\nYour total is ₱{total_cost:.2f}. Please enter the cash rendered: ₱"))
        
        if cash_rendered < total_cost:
            print("Insufficient funds. Please enter a valid amount.")
        else:
            change = cash_rendered - total_cost
            print(f"Payment accepted. Your change is: ₱{change:.2f}")
            break

# para mag run yung program
def main():
    menu = display_menu()
    while True:
        order_item, total_cost = take_order(menu)
        
        if order_item is None:  # pag gusto umalis ng user
            break
        
        process_payment(total_cost)
        another_order = input("\nWould you like to place another order? (yes/no): ").lower()
        if another_order != 'yes':
            print("Thank you for your order! Have a great day!")
            break

if __name__ == "__main__":
    main()

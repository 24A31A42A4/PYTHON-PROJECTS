import qrcode
import time

def add_items_cart(cart, cost, parts):
    number = int(input("Enter how many products to add in cart: "))
    for i in range(number):
        key = input("Enter item name to add in cart (check available products first): ")
        if key in parts:
            value = int(input(f"Enter quantity of the {key}: "))
            if key in cart:
                cart[key]+=value
            else:
                cart[key]=value
            cost = cost + parts[key]['price'] * value
            print("Items added successfully.")
        else:
            print("The product you have chosen is out of stock. When it is back, we will contact you.")
    return cost
def remove_items_cart(cart, cost, parts):
    print(cart)
    remove_item = input("Enter item you want to remove: ")
    if remove_item in cart:
        quantity = cart[remove_item]
        cost -= parts[remove_item]['price'] * quantity
        del cart[remove_item]
        print("Item removed successfully.")
    else:
        print("The item is not present in the cart.")
    print("Current total cost:", cost)
    return cost
def view_items_cart(cart, cost, parts):
    print("\nItems in cart:")
    if len(cart) == 0:
        print("Your cart is empty.")
    else:
        for item, qty in cart.items():
            price = parts[item]['price']
            print(f"{item} - Quantity: {qty}, Price per unit: {price}, Total cost of the {item}: {price * qty}")
    print(f"Total Amount: {cost}")
    check = input("Do you want to buy the products in your cart? : ")
    if check == "yes":
        address = input("Enter valid address to deliver the product: ")
        payment_method = input("Payment method (Cash / UPI Method): ").lower()
        if payment_method == "cash":
            print("Pay after taking delivery")
        else:
            qr = qrcode.QRCode()
            qr.add_data(f"Amount: {cost}")
            qr.add_data(f"  Delivery Address: {address}")
            qr.make()
            qr.print_ascii()
            print("Pay the money. QR expires within 5 minutes")
            time.sleep(5)
            print("Thank you for shopping! Your order is placed.")
            cart.clear()
            return 0
    else:
        print("Continue shopping")
def clear_all_items(cart, cost, parts):
    cart.clear()
    cost = 0
    return cost

cart = {}
parts = {}
cost = 0

while True:
    with open("data.txt", "r") as f:
        next(f)
        for line in f:
            pid, name, price, stock = line.strip().split(",")
            parts[name] = {'price': float(price), 'stock': int(stock)}
    print("In my store, these products are available:")
    for i in parts:
        print(i)
    c = int(input("\nEnter choice:\n1. Add Items\n2. Remove Items\n3. Clear Items\n4. View Items\n5. Exit\nChoice: "))
    if c == 1:
        cost = add_items_cart(cart, cost, parts)
    elif c == 2:
        cost = remove_items_cart(cart, cost, parts)
    elif c == 3:
        cost = clear_all_items(cart, cost, parts)
    elif c == 4:
        view_items_cart(cart, cost, parts)
    elif c == 5:
        print("Exit")
        break
    else:
        print("Invalid input")
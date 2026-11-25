print("Retail Billing System")
print("=====================")

while True:
    try:
        number_of_products = int(input("How many products do you want to purchase? "))
        if number_of_products > 0:
            break
        print("Please enter a number greater than zero.")
    except ValueError:
        print("Please enter a valid whole number.")

tax_rates = {"Food": 0.05, "Clothing": 0.12, "Electronics": 0.18}
items = []

for i in range(1, number_of_products + 1):
    print(f"\nProduct {i}")
    product_name = input("Enter product name: ").strip()

    while True:
        category = input("Enter category (Food / Clothing / Electronics): ").strip().title()
        if category in tax_rates:
            break
        print("Invalid category. Choose Food, Clothing, or Electronics.")

    while True:
        try:
            price = float(input("Enter price per unit: "))
            if price > 0:
                break
            print("Price must be greater than zero.")
        except ValueError:
            print("Please enter a valid price.")

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                break
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a valid whole number.")

    line_price = price * quantity
    tax = line_price * tax_rates[category]
    items.append((product_name, category, quantity, line_price, tax))

subtotal = sum(item[3] for item in items)
total_tax = sum(item[4] for item in items)
discount = min(subtotal * 0.10, 1000) if subtotal >= 5000 else 0
final_amount = subtotal + total_tax - discount

print("\n==================== ITEMIZED INVOICE ====================")
print("{:<18} {:<12} {:>6} {:>12} {:>12} {:>12}".format(
    "Product", "Category", "Qty", "Price (Rs)", "Tax (Rs)", "Final (Rs)"
))
print("-" * 78)

for product_name, category, quantity, line_price, tax in items:
    print("{:<18} {:<12} {:>6} {:>12.2f} {:>12.2f} {:>12.2f}".format(
        product_name, category, quantity, line_price, tax, line_price + tax
    ))

print("-" * 78)
print("{:<48} Rs {:>12.2f}".format("Subtotal:", subtotal))
print("{:<48} Rs {:>12.2f}".format("Total Tax:", total_tax))
print("{:<48} Rs {:>12.2f}".format("Discount:", discount))
print("{:<48} Rs {:>12.2f}".format("FINAL AMOUNT:", final_amount))
print("==========================================================")

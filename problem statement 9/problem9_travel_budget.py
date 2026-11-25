# Travel Budget Analysis

while True:
    try:
        travel_budget = float(input("Enter your travel budget in Indian Rupees (INR): "))
        if travel_budget > 0:
            break
        print("The budget must be positive.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        category_count = int(input("How many expense categories are planned? "))
        if category_count > 0:
            break
        print("Enter at least one expense category.")
    except ValueError:
        print("Please enter a whole number.")

category_names = []
foreign_amounts = []
exchange_rates = []
category_totals = []

for category_number in range(category_count):
    print("\nExpense category", category_number + 1)
    category_name = input("Enter the expense category name: ")

    while True:
        try:
            foreign_amount = float(input("Enter the amount in foreign currency: "))
            if foreign_amount > 0:
                break
            print("The amount must be positive.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            exchange_rate = float(input("Enter the exchange rate (INR for one unit): "))
            if exchange_rate > 0:
                break
            print("The exchange rate must be positive.")
        except ValueError:
            print("Please enter a valid number.")

    converted_amount = foreign_amount * exchange_rate
    category_total = converted_amount + converted_amount * 0.02

    category_names.append(category_name)
    foreign_amounts.append(foreign_amount)
    exchange_rates.append(exchange_rate)
    category_totals.append(category_total)

total_expense = sum(category_totals)
largest_expense_index = 0

for category_index in range(category_count):
    if category_totals[category_index] > category_totals[largest_expense_index]:
        largest_expense_index = category_index

print("\n--- Expense Summary ---")
for category_index in range(category_count):
    converted_amount = foreign_amounts[category_index] * exchange_rates[category_index]
    conversion_fee = converted_amount * 0.02

    print("\nCategory:", category_names[category_index])
    print("Foreign currency amount:", format(foreign_amounts[category_index], ".2f"))
    print("Exchange rate (INR per unit):", format(exchange_rates[category_index], ".2f"))
    print("Converted amount (INR):", format(converted_amount, ".2f"))
    print("2% conversion fee (INR):", format(conversion_fee, ".2f"))
    print("Category total (INR):", format(category_totals[category_index], ".2f"))

print("\nTotal expense (INR):", format(total_expense, ".2f"))
print("Travel budget (INR):", format(travel_budget, ".2f"))
print("Largest expense category:", category_names[largest_expense_index])
print("Largest category total (INR):", format(category_totals[largest_expense_index], ".2f"))

if total_expense <= travel_budget:
    print("You are within your travel budget.")
else:
    print("You have exceeded your travel budget.")

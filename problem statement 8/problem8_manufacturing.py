print("Manufacturing Cost and Profitability Analysis")

product_name = input("Enter the product name: ")

prompts = [
    "Enter quantity produced: ",
    "Enter material cost per unit: ",
    "Enter labour cost per unit: ",
    "Enter machine cost: ",
    "Enter wastage percentage: ",
    "Enter selling price per unit: "
]

values = []

# Read all numeric inputs using one loop.
for prompt in prompts:
    value = float(input(prompt))
    values.append(value)

quantity_produced = values[0]
material_cost_per_unit = values[1]
labour_cost_per_unit = values[2]
machine_cost = values[3]
wastage_percentage = values[4]
selling_price_per_unit = values[5]

# Calculate production costs.
total_material_cost = quantity_produced * material_cost_per_unit
wastage_cost = total_material_cost * wastage_percentage / 100
total_labour_cost = quantity_produced * labour_cost_per_unit
total_production_cost = total_material_cost + wastage_cost + total_labour_cost + machine_cost

# Calculate sales and profit or loss.
total_sales_revenue = quantity_produced * selling_price_per_unit
profit_or_loss = total_sales_revenue - total_production_cost

print("\n--- Cost and Profitability Details ---")
print("Product:", product_name)
print("Quantity produced:", quantity_produced)
print("Total material cost: {:.2f}".format(total_material_cost))
print("Wastage cost: {:.2f}".format(wastage_cost))
print("Total labour cost: {:.2f}".format(total_labour_cost))
print("Machine cost: {:.2f}".format(machine_cost))
print("Total production cost: {:.2f}".format(total_production_cost))
print("Total sales revenue: {:.2f}".format(total_sales_revenue))

if profit_or_loss > 0:
    print("Profit: {:.2f}".format(profit_or_loss))
elif profit_or_loss < 0:
    print("Loss: {:.2f}".format(abs(profit_or_loss)))
else:
    print("Result: Break-even (no profit or loss)")

# Calculate profit percentage only when production cost is greater than zero.
if total_production_cost > 0:
    profit_percentage = profit_or_loss / total_production_cost * 100
    print("Profit percentage: {:.2f}%".format(profit_percentage))

    if profit_percentage >= 15:
        print("15% illustrative profit target: Met")
    else:
        print("15% illustrative profit target: Not met")
else:
    print("Profit percentage: Not applicable (total production cost is zero)")
    print("15% illustrative profit target: Cannot be evaluated with zero production cost")

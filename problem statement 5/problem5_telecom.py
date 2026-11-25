plans = [
    ["Basic", 199, 2, 28],
    ["Smart", 299, 5, 28],
    ["Premium", 399, 10, 56],
    ["Max", 599, 20, 84],
]


def read_number(prompt, error, integer=False):
    while True:
        try:
            value = int(input(prompt)) if integer else float(input(prompt))
            if value >= 0:
                return value
            print(error)
        except ValueError:
            print("Please enter a valid whole number." if integer else "Please enter a valid number.")


required_data = read_number(
    "Enter required data in GB: ",
    "Please enter a non-negative number.",
)
required_validity = read_number(
    "Enter required validity in days: ",
    "Please enter a non-negative number of days.",
    integer=True,
)
maximum_budget = read_number(
    "Enter maximum budget in rupees: ",
    "Please enter a non-negative amount.",
)

eligible_plans = []
for name, price, included_data, validity in plans:
    extra_data = max(0, required_data - included_data)
    extra_charge = extra_data * 20
    total_cost = price + extra_charge
    if validity >= required_validity and total_cost <= maximum_budget:
        eligible_plans.append([name, price, included_data, validity, extra_data, extra_charge, total_cost])

if not eligible_plans:
    print("\nNo plans meet your data, validity, and budget requirements.")
else:
    print("\nEligible plans:")
    for name, price, included_data, validity, extra_data, extra_charge, total_cost in eligible_plans:
        print(
            f"- {name}: Rs. {price} base price, {included_data} GB data, "
            f"{validity} days validity"
        )
        print(
            f"  Extra data: {extra_data:.2f} GB; "
            f"extra charge: Rs. {extra_charge:.2f}; total cost: Rs. {total_cost:.2f}"
        )

    cheapest_plan = min(eligible_plans, key=lambda plan: plan[6])
    print(
        f"\nCheapest eligible plan: {cheapest_plan[0]} "
        f"at a total cost of Rs. {cheapest_plan[6]:.2f}."
    )

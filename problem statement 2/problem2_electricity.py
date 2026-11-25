def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Enter a valid whole number greater than zero.")


def read_units(month):
    while True:
        try:
            units = float(input(f"Enter electricity units for month {month}: "))
            if units >= 0:
                return units
        except ValueError:
            pass
        print("Units cannot be negative.")


def calculate_bill(units):
    if units <= 100:
        energy_charge = units * 1.50
    elif units <= 200:
        energy_charge = 150 + (units - 100) * 2.50
    else:
        energy_charge = 400 + (units - 200) * 4

    subtotal = energy_charge + 50
    surcharge = subtotal * 0.05
    rebate = (subtotal + surcharge) * 0.02 if units < 100 else 0
    return energy_charge, surcharge, rebate, subtotal + surcharge - rebate


print("Progressive Electricity Billing")
number_of_months = read_positive_int("Enter the number of months: ")

previous_bill = None
print("\nMonthly Electricity Bills")

for month in range(1, number_of_months + 1):
    units = read_units(month)
    energy, surcharge, rebate, final_bill = calculate_bill(units)

    print(f"\nMonth {month}")
    print(f"  Units consumed:  {units:.2f}")
    print(f"  Energy charge:   Rs. {energy:.2f}")
    print("  Fixed charge:    Rs.50.00")
    print(f"  Surcharge (5%):  Rs. {surcharge:.2f}")
    print(f"  Rebate:          Rs. {rebate:.2f}")
    print(f"  Final bill:      Rs. {final_bill:.2f}")

    if previous_bill is not None:
        change = final_bill - previous_bill
        if previous_bill:
            change_percent = change / previous_bill * 100
            print(f"\nMonth {month - 1} to month {month}: change Rs. {change:.2f} ({change_percent:.2f}%)")
            if change_percent > 25:
                print("  Unusual increase: bill increased by more than 25%.")
        else:
            print(f"\nMonth {month - 1} to month {month}: change Rs. {change:.2f}")

    previous_bill = final_bill

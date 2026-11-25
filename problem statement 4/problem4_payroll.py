def get_non_negative_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount >= 0:
                return amount
            print("Amount cannot be negative.")
        except ValueError:
            print("Please enter a valid amount.")


name = input("Enter employee name: ")
salary = [
    get_non_negative_amount("Enter basic salary (Rs.): "),
    get_non_negative_amount("Enter allowances (Rs.): "),
    get_non_negative_amount("Enter overtime amount (Rs.): "),
    get_non_negative_amount("Enter incentives (Rs.): "),
]
gross = sum(salary)

deduction = (
    0 if gross <= 20000
    else (gross - 20000) * 0.05 if gross <= 50000
    else 1500 + (gross - 50000) * 0.10
)
net = gross - deduction

print("\n========== Salary Statement ==========")
print(f"Employee name:   {name}")
for label, amount in zip(("Basic salary", "Allowances", "Overtime", "Incentives"), salary):
    print(f"{label + ':':16}Rs. {amount:,.2f}")
print("--------------------------------------")
print(f"Gross salary:    Rs. {gross:,.2f}")
print(f"Total deduction: Rs. {deduction:,.2f}")
print(f"Net salary:      Rs. {net:,.2f}")
print("======================================")

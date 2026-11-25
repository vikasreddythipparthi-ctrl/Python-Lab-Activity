# Keep asking until the user enters a valid amount.
def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount >= 0 and amount < float("inf"):
                return amount
            print("Enter a finite amount that is zero or greater.")
        except ValueError:
            print("Enter a valid number.")


event_name = input("Enter the event name: ").strip()
while event_name == "":
    print("The event name cannot be blank.")
    event_name = input("Enter the event name: ").strip()

print("\nEnter fixed expenses:")
venue_cost = get_amount("Venue cost: $")
equipment_cost = get_amount("Equipment cost: $")
transport_cost = get_amount("Transport cost: $")

print("\nEnter expenses for each participant:")
catering_cost = get_amount("Catering cost per participant: $")
certificate_cost = get_amount("Certificate cost per participant: $")

print("\nEnter event estimates:")
while True:
    try:
        participants = int(input("Expected number of participants: "))
        if participants >= 0:
            break
        print("Enter a whole number that is zero or greater.")
    except ValueError:
        print("Enter a valid whole number.")

registration_fee = get_amount("Registration fee per participant: $")
sponsorship = get_amount("Sponsorship amount: $")

# Add the expenses and income.
fixed_expenses = venue_cost + equipment_cost + transport_cost
variable_cost_per_person = catering_cost + certificate_cost
total_variable_expenses = variable_cost_per_person * participants
total_event_expenses = fixed_expenses + total_variable_expenses
registration_income = registration_fee * participants
total_income = registration_income + sponsorship
profit_or_loss = total_income - total_event_expenses

# Calculate how many registrations cover fixed expenses after sponsorship.
if registration_fee <= variable_cost_per_person:
    break_even_text = "Not achievable: fee does not cover participant costs."
elif fixed_expenses <= sponsorship:
    break_even_text = "0 registrations (sponsorship covers fixed expenses)."
else:
    contribution_per_person = registration_fee - variable_cost_per_person
    amount_to_cover = fixed_expenses - sponsorship
    break_even_registrations = amount_to_cover / contribution_per_person

    # int() drops the decimal part, so add one if registrations are still needed.
    break_even_registrations = int(break_even_registrations)
    if break_even_registrations * contribution_per_person < amount_to_cover:
        break_even_registrations = break_even_registrations + 1

    break_even_text = str(break_even_registrations) + " registrations"

# Show any amount by which total income falls short of total expenses.
if total_income < total_event_expenses:
    shortfall = total_event_expenses - total_income
else:
    shortfall = 0

# Print the financial report.
print("\n--- Financial Report: " + event_name + " ---")
print(f"Total fixed expenses:          ${fixed_expenses:.2f}")
print(f"Total variable expenses:       ${total_variable_expenses:.2f}")
print(f"Total event expenses:          ${total_event_expenses:.2f}")
print(f"Registration income:           ${registration_income:.2f}")
print(f"Sponsorship income:             ${sponsorship:.2f}")
print(f"Total income:                   ${total_income:.2f}")

if profit_or_loss >= 0:
    print(f"Final profit:                   ${profit_or_loss:.2f}")
else:
    print(f"Final loss:                     ${abs(profit_or_loss):.2f}")

print(f"Sponsorship/funding shortfall: ${shortfall:.2f}")
print("Break-even registrations:      " + break_even_text)

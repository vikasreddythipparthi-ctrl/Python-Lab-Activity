print("Railway Fare and Reservation Calculator")


def get_number(prompt, number_type, valid):
    while True:
        try:
            value = number_type(input(prompt))
            if valid(value):
                return value
        except ValueError:
            pass
        print("Invalid input.")


distance = get_number(
    "Enter journey distance in kilometres: ",
    float,
    lambda value: value > 0,
)
passenger_count = get_number(
    "Enter number of passengers: ",
    int,
    lambda value: value > 0,
)

print("\n1. Sleeper - Rs. 1/km\n2. AC - Rs. 2/km\n3. Chair Car - Rs. 1.50/km")
classes = {"1": ("Sleeper", 1.0), "2": ("AC", 2.0), "3": ("Chair Car", 1.5)}
while True:
    choice = input("Choose a class (1, 2, or 3): ").strip()
    if choice in classes:
        class_name, rate = classes[choice]
        break
    print("Please choose 1, 2, or 3.")

passenger_details = []
for number in range(1, passenger_count + 1):
    print("\nPassenger", number)
    name = input("Enter passenger name: ").strip()
    while not name:
        name = input("Name cannot be empty. Enter passenger name: ").strip()
    age = get_number("Enter passenger age: ", int, lambda value: value >= 0)

    fare = distance * rate
    if age < 5:
        fare = 0
    elif age <= 11:
        fare *= 0.5
    elif age >= 60:
        fare *= 0.9
    passenger_details.append((name, fare + 40))

cancelled = input("\nIs the ticket cancelled? (yes/no): ").strip().lower()
while cancelled not in ("yes", "no"):
    cancelled = input("Please enter yes or no: ").strip().lower()

total = sum(fare for _, fare in passenger_details)
print("\nFare details")
print("Travel class:", class_name)
for name, fare in passenger_details:
    print(name, "- Rs.", f"{fare:.2f}")

print("Total ticket amount: Rs.", f"{total:.2f}")
if cancelled == "yes":
    penalty = total * 0.25
    print("Cancellation penalty (25%): Rs.", f"{penalty:.2f}")
    print("Amount payable after cancellation: Rs.", f"{penalty:.2f}")
else:
    print("Total amount payable: Rs.", f"{total:.2f}")

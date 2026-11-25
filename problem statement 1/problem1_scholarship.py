print("UNIVERSITY SCHOLARSHIP ALLOCATION")
print("Eligibility: aggregate >= 80%, every subject >= 60%,")
print("attendance >= 75%, and annual family income <= Rs. 3,00,000.\n")


def number(prompt, maximum=None, positive=True):
    while True:
        try:
            value = float(input(prompt))
            if (value > 0 if positive else value >= 0) and (
                maximum is None or value <= maximum
            ):
                return value
        except ValueError:
            pass
        print("Invalid input.")


def whole_number(prompt):
    while True:
        value = number(prompt)
        if value.is_integer():
            return int(value)
        print("Please enter a whole number.")


def main():
    student_count = whole_number("How many students are applying? ")
    subject_count = whole_number("How many subjects should be entered for each student? ")
    eligible = []
    non_eligible = []

    for student_number in range(1, student_count + 1):
        print("\nEnter details for student", student_number)
        name = input("Student name: ").strip()
        while not name:
            name = input("Name cannot be empty. Enter student name: ").strip()

        aggregate = number("Aggregate marks percentage: ", 100)
        subjects = [
            number(f"Marks percentage in subject {i + 1}: ", 100)
            for i in range(subject_count)
        ]
        attendance = number("Attendance percentage: ", 100)
        income = number("Annual family income (Rs.): ", positive=False)

        if aggregate >= 80 and min(subjects) >= 60 and attendance >= 75 and income <= 300000:
            eligible.append((aggregate, attendance, income, name))
        else:
            non_eligible.append(name)

    eligible.sort(key=lambda student: (-student[0], -student[1], student[2]))

    print("\nELIGIBLE STUDENTS")
    if eligible:
        for rank, (aggregate, attendance, income, name) in enumerate(eligible, 1):
            print(
                f"{rank}. {name} | Aggregate: {aggregate:.2f}% | "
                f"Attendance: {attendance:.2f}% | Annual income: Rs. {income:.2f}"
            )
    else:
        print("No students met all the eligibility conditions.")

    print("\nNON-ELIGIBLE STUDENTS")
    if non_eligible:
        print(*non_eligible, sep="\n")
    else:
        print("All students met the eligibility conditions.")


if __name__ == "__main__":
    main()

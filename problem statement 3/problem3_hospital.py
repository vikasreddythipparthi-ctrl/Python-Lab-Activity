patient_name = input("Enter the patient's name: ")
age = int(input("Enter the patient's age: "))
consultation_charges = float(input("Enter consultation charges (Rs.): "))
diagnostic_charges = float(input("Enter diagnostic charges (Rs.): "))
treatment_charges = float(input("Enter treatment charges (Rs.): "))
family_income = float(input("Enter annual family income (Rs.): "))

if (age < 0 or consultation_charges < 0 or diagnostic_charges < 0
        or treatment_charges < 0 or family_income < 0):
    print("Invalid input: age, income, and charges cannot be negative.")
else:
    consultation_discount = consultation_charges * 0.10 if age >= 60 else 0
    treatment_discount = treatment_charges * 0.05 if family_income < 150000 else 0
    total_charges = consultation_charges + diagnostic_charges + treatment_charges
    total_discounts = consultation_discount + treatment_discount
    final_bill = total_charges - total_discounts
    bill_category = "Normal bill" if final_bill < 5000 else ("Medium bill" if final_bill <= 10000 else "High bill")

    print("\n--- Hospital Itemized Bill ---")
    print("Patient name:", patient_name)
    print("Age:", age)
    print("Consultation charges: Rs.", format(consultation_charges, ".2f"))
    print("Consultation discount: -Rs.", format(consultation_discount, ".2f"))
    print("Diagnostic charges: Rs.", format(diagnostic_charges, ".2f"))
    print("Treatment charges: Rs.", format(treatment_charges, ".2f"))
    print("Treatment discount: -Rs.", format(treatment_discount, ".2f"))
    print("Total charges: Rs.", format(total_charges, ".2f"))
    print("Total discounts: -Rs.", format(total_discounts, ".2f"))
    print("Final bill: Rs.", format(final_bill, ".2f"))
    print("Patient classification:", bill_category)


class Patient:
    def __init__(
        self, patient_id, name, age, gender, phone,
        reason_for_visit, symptoms, visit_date
    ):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.reason_for_visit = reason_for_visit
        self.symptoms = symptoms
        self.visit_date = visit_date

    def display_info(self):
        print("\n===== PATIENT DETAILS =====")
        print("Patient ID:", self.patient_id)
        print("Full Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Phone Number:", self.phone)
        print("Reason for Visit:", self.reason_for_visit)
        print("Symptoms/Injury:", self.symptoms)
        print("Visit Date:", self.visit_date)

    def update_record(self):
        while True:
            print("\n===== UPDATE PATIENT RECORD =====")
            print("1. Update full name")
            print("2. Update age")
            print("3. Update gender")
            print("4. Update phone number")
            print("5. Update reason for visit")
            print("6. Update symptoms/injury")
            print("7. Update visit date")
            print("8. Finish updating")

            choice = input("Choose a detail to update (1-8): ")

            if choice == "1":
                new_name = input("Enter the correct full name: ").strip()
                if new_name:
                    self.name = new_name
                    print("Name updated successfully.")
                else:
                    print("Name cannot be empty.")

            elif choice == "2":
                try:
                    new_age = int(input("Enter the correct age: "))
                    if new_age < 0:
                        print("Age cannot be negative.")
                    else:
                        self.age = new_age
                        print("Patient age updated successfully.")
                except ValueError:
                    print("Please enter a valid whole number.")

            elif choice == "3":
                new_gender = input("Enter the correct gender: ").strip()
                if new_gender:
                    self.gender = new_gender
                    print("Gender updated successfully.")
                else:
                    print("Gender cannot be empty.")

            elif choice == "4":
                self.phone = input(
                    "Enter the correct phone number: "
                ).strip()
                print("Phone number updated successfully.")

            elif choice == "5":
                self.reason_for_visit = input(
                    "Enter the correct reason for visit: "
                ).strip()
                print("Reason for visit updated successfully.")

            elif choice == "6":
                self.symptoms = input(
                    "Enter the correct symptoms or injury: "
                ).strip()
                print("Symptoms/injury updated successfully.")

            elif choice == "7":
                self.visit_date = input(
                    "Enter the correct visit date: "
                ).strip()
                print("Visit date updated successfully.")

            elif choice == "8":
                print("Finished updating patient record.")
                break

            else:
                print("Invalid choice. Select 1-8.")


class PatientRecordSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        if self.find_patient(patient.patient_id) is not None:
            print("Patient ID already exists.")
            return

        self.patients.append(patient)
        print("Patient record added successfully.")

    def display_all_patients(self):
        if not self.patients:
            print("No patient records found.")
            return

        for patient in self.patients:
            patient.display_info()
            print("----------------------------")

    def find_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def search_patient(self):
        patient_id = input("Enter patient ID to search: ").strip()
        patient = self.find_patient(patient_id)

        if patient:
            patient.display_info()
        else:
            print("Patient not found.")

    def edit_patient_record(self):
        patient_id = input(
            "Enter the patient ID whose record you want to update: "
        ).strip()

        patient = self.find_patient(patient_id)

        if patient:
            print("\nCurrent patient details:")
            patient.display_info()

            patient.update_record()

            print("\nUpdated patient details:")
            patient.display_info()
        else:
            print("Patient not found. Please check the patient ID.")


# Create the patient record system
record_system = PatientRecordSystem()

while True:
    print("\n===== HOSPITAL PATIENT RECORD SYSTEM =====")
    print("1. Register a new patient")
    print("2. Display all patient records")
    print("3. Search for a patient")
    print("4. Update any patient record")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        patient_id = input("Enter patient ID: ").strip()

        if not patient_id:
            print("Patient ID is required.")
            continue

        if record_system.find_patient(patient_id) is not None:
            print("Patient ID already exists.")
            continue

        name = input("Enter full name: ").strip()

        if not name:
            print("Patient name is required.")
            continue

        try:
            age = int(input("Enter age: "))

            if age < 0:
                print("Age cannot be negative.")
                continue

        except ValueError:
            print("Please enter a valid whole number for age.")
            continue

        gender = input("Enter gender: ").strip()
        phone = input("Enter phone number: ").strip()
        reason = input("Reason for hospital visit: ").strip()
        symptoms = input("Describe symptoms or injury: ").strip()
        visit_date = input("Enter visit date: ").strip()

        patient = Patient(
            patient_id, name, age, gender, phone,
            reason, symptoms, visit_date
        )

        record_system.add_patient(patient)

    elif choice == "2":
        record_system.display_all_patients()

    elif choice == "3":
        record_system.search_patient()

    elif choice == "4":
        record_system.edit_patient_record()

    elif choice == "5":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Select 1-5.")

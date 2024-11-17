#Capstone Project 1 - Data Pasien Rumah Sakit
import os

patients = {
    "patient_1" : {
        "name" : "Andi Surandi",
        "age" : 27,
        "gender" : "Laki-Laki",
        "contact_info" : "081234567890",
        "appointment_date" : "01-01-2023",
        "diagnosis" : "Bronchitis",
        "doctor" : "Dr. Budi"
    },
    "patient_2" : {
        "name" : "Sumiyati",
        "age" : 56,
        "gender" : "Perempuan",
        "diagnosis" : "Diabetes",
        "appointment_date" : "03-06-2023",
        "contact_info" : "081122334899",
        "doctor" : "Dr. Mariska"
    },
    "patient_3" : {
        "name" : "Kenzi Suwono",
        "age" : 13,
        "gender" : "Laki-Laki",
        "contact_info" : "081112233889",
        "appointment_date" : "01-01-2023",
        "diagnosis" : "Flu Berat",
        "doctor" : "Dr. Hartono"
    }
}

def val_cannot_empty(value):
    if len(value) == 0:
        raise ValueError("Value cannot be empty")
    return value

def val_must_digit(value):
    if not value.isdigit():
        raise ValueError("Value must be a digit")
    return int(value)

def val_gender(value):
    if value not in ["L", "P"]:
        raise ValueError("Gender must be 'L' or 'P'")
    return value

def val_date(value):
    day, month, year = value.split("-")

    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        raise ValueError("Date must be in DD-MM-YYYY format.")
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        raise ValueError("Date must be in DD-MM-YYYY format.")
    
    day, month, year = int(day), int(month), int(year)
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31.")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    if not (1900 < year <= 2024):
        raise ValueError("Year must be between 1900 and 2024.")
    
    return value

def get_valid_input(prompt, val_funct):
    try:
        value = val_funct(input(prompt))
        return value
    except ValueError as e:
        print(f"Error: {e}")
        return get_valid_input(prompt, val_funct)

def show_patient():
    if len(patients) == 0:
        print("No patient data available.")
        return
    
    print("\n--- Patient Data ---")
    print("ID\t\t | Name\t\t | Age\t | Gender\t")
    for patient_id, patient_data in patients.items():
        print(f"{patient_id}\t | {patient_data['name']}\t | {patient_data['age']}\t | {patient_data['gender']}\t")
    
    view_details = get_valid_input("\nDo you want to view details of a specific patient? (yes/no): ", val_cannot_empty)
    if view_details.lower() == "yes":
        patient_id = get_valid_input("Enter the ID of the patient you want to view details: ", val_cannot_empty)
        if patient_id in patients:
            patient_data = patients[patient_id]
            print("ID\t\t | Name\t\t | Age\t | Gender\t | Diagnosis\t | Appointment Date\t | Contact Info\t\t | Doctor\t ")
            print(f"{patient_id}\t | {patient_data['name']}\t | {patient_data['age']}\t | {patient_data['gender']}\t | {patient_data['diagnosis']}\t | {patient_data['appointment_date']}\t\t | {patient_data['contact_info']}\t\t | {patient_data['doctor']}\t")

def show_all_patientinfo():
    print("\n--- Patient Data ---")
    print("ID\t\t | Name\t\t | Age\t | Gender\t")
    for patient_id, patient_data in patients.items():
        print(f"{patient_id}\t | {patient_data['name']}\t | {patient_data['age']}\t | {patient_data['gender']}\t | {patient_data['diagnosis']}\t | {patient_data['appointment_date']}\t\t | {patient_data['contact_info']}\t\t | {patient_data['doctor']}\t")

def add_patient():
    patient_id = f"patient_{len(patients) + 1}"

    print("\n--- Add New Patient ---")
    name = get_valid_input("Enter patient's name: ", val_cannot_empty)
    age = get_valid_input("Enter patient's age: ", val_must_digit)
    gender = get_valid_input("Enter patient's gender (L/P): ", val_gender)
    gender = "Laki-Laki" if gender == "L" else "Perempuan"
    contact_info = get_valid_input("Enter contact information: ", val_cannot_empty)
    diagnosis = get_valid_input("Enter patient's diagnosis: ", val_cannot_empty)
    appointment_date = get_valid_input("Enter admission date (DD-MM-YYYY): ", val_date)
    assigned_doctor = get_valid_input("Enter assigned doctor's name: ", val_cannot_empty)

    patients[patient_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "contact_info": contact_info,
        "appointment_date": appointment_date,
        "diagnosis": diagnosis,
        "doctor": assigned_doctor
    }

    print(f"\n{patient_id} added successfully!\n")
    show_all_patientinfo()

def update_patient():
    show_all_patientinfo()
    patient_id = get_valid_input("Enter the ID of the patient you want to update: ", val_cannot_empty)
    if patient_id in patients:
        patient_data = patients[patient_id]
        choice = 0
        while choice != 8:
            os.system("cls")
            print("ID\t\t | Name\t\t | Age\t | Gender\t | Diagnosis\t | Appointment Date\t | Contact Info\t\t | Doctor\t ")
            print(f"{patient_id}\t | {patient_data['name']}\t | {patient_data['age']}\t | {patient_data['gender']}\t | {patient_data['diagnosis']}\t | {patient_data['appointment_date']}\t\t | {patient_data['contact_info']}\t\t | {patient_data['doctor']}\t")
    
            print("\nChoose data to update:")
            print("1. Name")
            print("2. Age")
            print("3. Gender")
            print("4. Diagnosis")
            print("5. Appointment Date")
            print("6. Contact Info")
            print("7. Doctor")
            print("8. Finish Updating")

            choice = int(get_valid_input("Enter your choice: ", val_must_digit))

            match choice:
                case 1:
                    patient_data['name'] = get_valid_input("Enter new name: ", val_cannot_empty)
                case 2:
                    patient_data['age'] = get_valid_input("Enter new age: ", val_must_digit)
                case 3:
                    gender = get_valid_input("Enter new gender (L/P): ", val_gender)
                    patient_data['gender'] = "Laki-Laki" if gender == "L" else "Perempuan"
                case 4:
                    patient_data['diagnosis'] = get_valid_input("Enter new diagnosis: ", val_cannot_empty)
                case 5:
                    patient_data['appointment_date'] = get_valid_input("Enter new appointment date (DD-MM-YYYY): ", val_date)
                case 6:
                    patient_data['contact_info'] = get_valid_input("Enter new contact information: ", val_cannot_empty)
                case 7:
                    patient_data['doctor'] = get_valid_input("Enter new doctor's name: ", val_cannot_empty)
                case 8:
                    break
                case _:
                    print("Invalid input. Please enter a number between 1 and 8.")
            
            print(f"\n{patient_id} updated successfully!\n")
            input("Press Enter to continue...")
    
    else:
        print(f"\n{patient_id} not found!\n")
         
def delete_patient():
    show_all_patientinfo()
    print("\n--- Delete Patient Data ---")
    patient_id = get_valid_input("Enter the ID of the patient you want to delete: ", val_cannot_empty)
    if patient_id in patients:
        confirm = get_valid_input(f"Are you sure you want to delete {patient_id}? (yes/no): ", val_cannot_empty)
        if confirm == "yes":
            del patients[patient_id]
            print(f"\n{patient_id} deleted successfully!\n")
            show_all_patientinfo()
        else:
            print("Deletion canceled.\n")
            show_all_patientinfo()
    else:
        print(f"\n{patient_id} not found!\n")


menu = 0
while menu != 5:
    os.system("cls")
    print("--- Hospital Patient Management System ---")
    print("==========================================")
    print("List menu: ")
    print("1. View Patient Data")
    print("2. Add a NewPatient Data")
    print("3. Update Patient Data")
    print("4. Delete Patient Data")
    print("5. Exit")

    menu = int(get_valid_input("Please Select The Number of Menu: ", val_must_digit))

    match menu:
        case 1:
            show_patient()
        case 2:
            add_patient()
        case 3:
            update_patient()
        case 4:
            delete_patient()
        case 5: 
            print("Exiting the program...")
        case _:
            print("Invalid input. Please enter a number between 1 and 5.")

    input("Press Enter to continue...") 


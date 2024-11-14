#Capstone Project 1 - Data Pasien Rumah Sakit
import os

patients = {
    "patient_1" : {
        "name" : "Andi Surandi",
        "age" : 27,
        "gender" : "Laki-Laki",
        "diagnosis" : "Bronchitis",
        "appointment_date" : "01-01-2023",
        "contact_info" : "081234567890",
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
        "diagnosis" : "Flu Berat",
        "appointment_date" : "01-01-2023",
        "contact_info" : "0811122338899",
        "doctor" : "Dr. Hartono"
    }
}

def show_patient():
    print("\n--- Patient Data ---")
    print("ID\t\t | Name\t\t | Age\t | Gender\t")
    for patient_id, patient_data in patients.items():
        print(f"{patient_id}\t | {patient_data['name']}\t | {patient_data['age']}\t | {patient_data['gender']}\t")
    
    view_details = input("\nDo you want to view details of a specific patient? (yes/no): ")
    if view_details.lower() == "yes":
        patient_id = input("Enter the ID of the patient you want to view details: ")
        if patient_id in patients:
            print("ID\t\t | Name\t\t | Age\t | Gender\t | Diagnosis\t | Appointment Date\t | Contact Info\t\t | Doctor\t ")
            print(f"{patient_id}\t | {patient_data['name']}\t | {patient_data['age']}\t | {patient_data['gender']}\t | {patient_data['diagnosis']}\t | {patient_data['appointment_date']}\t\t | {patient_data['contact_info']}\t\t | {patient_data['doctor']}\t")


def add_patient():
    patient_id = f"patient_{len(patients) + 1}"

    print("\n--- Add New Patient ---")
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    gender = input("Enter patient's gender (Laki-Laki/Perempuan): ")
    diagnosis = input("Enter patient's diagnosis: ")
    appointment_date = input("Enter admission date (DD-MM-YYYY): ")
    contact_info = input("Enter contact information: ")
    assigned_doctor = input("Enter assigned doctor's name: ")

    patients[patient_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "diagnosis": diagnosis,
        "appointment_date": appointment_date,
        "contact_info": contact_info,
        "doctor": assigned_doctor
    }

    print(f"\n{patient_id} added successfully!\n")

def update_patient():
    patient_id = input("Enter the ID of the patient you want to update: ")
    if patient_id in patients:
        print("\n--- Update Patient Data ---")
        name = input("Enter patient's name: ")
        age = input("Enter patient's age: ")
        gender = input("Enter patient's gender (Laki-Laki/Perempuan): ")
        diagnosis = input("Enter patient's diagnosis: ")
        appointment_date = input("Enter admission date (DD-MM-YYYY): ")
        contact_info = input("Enter contact information: ")
        assigned_doctor = input("Enter assigned doctor's name: ")
    
        patients[patient_id] = {
            "name": name,
            "age": age,
            "gender": gender,
            "diagnosis": diagnosis,
            "appointment_date": appointment_date,
            "contact_info": contact_info,
            "doctor": assigned_doctor
        }
        print(f"\n{patient_id} updated successfully!\n")
    else:
        print(f"\n{patient_id} not found!\n")

def delete_patient():
    print("\n--- Delete Patient Data ---")
    patient_id = input("Enter the ID of the patient you want to delete: ")
    if patient_id in patients:
        confirm = input(f"Are you sure you want to delete {patient_id}? (yes/no): ")
        if confirm == "yes":
            del patients[patient_id]
            print(f"\n{patient_id} deleted successfully!\n")
        else:
            print("Deletion canceled.\n")
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

    try:
        menu = int(input("Please Select The Number of Menu: "))
    except:
        print("The Selected Menu Does Not Exist, Please Select The Existing Number of Menu")
        input("Press Enter to continue...") 
        continue

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

    input("Press Enter to continue...") 


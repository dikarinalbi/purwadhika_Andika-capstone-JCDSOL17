#Capstone Project 1 - Data Pasien Rumah Sakit
import os

patients = {
    "patient_1" : {
        "name" : "Andi Surandi",
        "age" : 27,
        "gender" : "Laki-Laki",
        "diagnosis" : "Bronchitis",
        "appointment_date" : "01-01-2023",
        "doctor" : "Dr. Budi"
    },
    "patient_2" : {
        "name" : "Sumiyati",
        "age" : 56,
        "gender" : "Perempuan",
        "diagnosis" : "Diabetes",
        "appointment_date" : "03-06-2023",
        "doctor" : "Dr. Mariska"
    },
    "patient_3" : {
        "name" : "Kenzi Suwono",
        "age" : 13,
        "gender" : "Laki-Laki",
        "diagnosis" : "Flu Berat",
        "appointment_date" : "01-01-2023",
        "doctor" : "Dr. Hartono"
    }
}

def show_patient():
    print("\n--- Patient Data ---")
    print("ID\t\t | Name\t\t | Age\t | Gender\t | Diagnosis\t | Appointment Date\t | Doctor\t ")
    for patient_id, patient_data in patients.items():
        print(f"{patient_id}\t | {patient_data['name']}\t | {patient_data['age']}\t | {patient_data['gender']}\t | {patient_data['diagnosis']}\t | {patient_data['appointment_date']}\t\t | {patient_data['doctor']}\t")


def add_patient():
    patient_id = f"patient_{len(patients) + 1}"

    print("\n--- Add New Patient ---")
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    gender = input("Enter patient's gender (Laki-Laki/Perempuan): ")
    diagnosis = input("Enter patient's diagnosis: ")
    admission_date = input("Enter admission date (DD-MM-YYYY): ")
    assigned_doctor = input("Enter assigned doctor's name: ")

    patients[patient_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "diagnosis": diagnosis,
        "admission_date": admission_date,
        "assigned_doctor": assigned_doctor
    }

    print(f"\nPatient {patient_id} added successfully!\n")


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
            pass
        case 4:
            pass
        case 5: 
            print("Exiting the program...")

    input("Press Enter to continue...") 


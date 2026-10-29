# Patient Record Management System

## 1. Project Description

The Patient Record Management System is a simple Python program designed to demonstrate object-oriented programming concepts. It allows users to add, display, search for, and update patient records.

## 2. Features

- Create patient records.
- Store multiple patient objects in a list.
- Display all patient records.
- Search for a patient using a unique ID.
- Update a patient's recorded condition.
- Display the total number of patient objects created.
- Validate input and prevent duplicate patient IDs.

## 3. Requirements

- Python 3
- A computer with a Python editor or terminal

## 4. How to Run

1. Save the source code as `patient_system.py`.
2. Open a terminal in the folder containing the file.
3. Run the command:

   `python patient_system.py`

## 5. Example Usage

The program displays a menu that allows users to add a patient, display records, search for a patient, update a condition, view the total number of records created, or exit.

Example test data:

- Patient ID: P001
- Name: Mary Johnson
- Age: 25
- Condition: Malaria

After entering the details, the program confirms that the record was added successfully.

## 6. Object-Oriented Programming

The `Patient` class defines the attributes and methods of a patient. Each patient record is an object created from this class.

Instance methods display and update individual patient information. A class method displays the number of patient objects created.

## 7. Data Structure

The program uses a Python list named `patients` to store multiple patient objects. The list can be looped through to display records, search for a patient, and update information.

## 8. Digital Public Goods (DPG) Alignment

- **Open-source readiness:** The project can be shared and reviewed through a GitHub repository.
- **Documentation:** The README explains the purpose, requirements, and usage of the software.
- **Privacy awareness:** Testing should use fictional patient information. Real medical information should not be stored in this educational program.
- **Accessibility:** The text-based menu provides simple instructions for users.
- **Reusability:** The program uses a straightforward structure that can be studied and extended.

This is an educational demonstration and is not a production-ready medical records system. It does not implement authentication, encryption, access controls, or secure database storage.

## 9. Limitations and Future Improvements

Future versions could include secure user authentication, persistent database storage, stronger privacy protections, and automated tests.

## 10. Conclusion

This project demonstrates Python classes, attributes, objects, methods, and list-based record management. It also provides basic documentation and identifies important privacy and security considerations.

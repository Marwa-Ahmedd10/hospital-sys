# This code implements a simple patient queue management system. 
# The program uses a list of lists to represent the queue, 
# where each sublist represents a specialization and can hold up to 10 patients. 
# The `add_patient` function prompts the user to enter 
#the specialization, patient name, and patient status (normal, urgent, or super urgent). 
# The function then adds the patient to the appropriate sublist in the queue based on their specialization
# and status. If the specialization is full, 
# the function prints an error message and does not add the patient to the queue.
# The `print_patients` function prints all patients in the queue, 
# sorted by status (super urgent patients first, then urgent patients, then normal patients). 
# The function iterates over each sublist in the queue, sorts the patients in that sublist by status, 
# and prints each patient's name.
# The `get_next_patient` function prompts the user to enter a specialization and removes the next patient 
# in the queue for that specialization. The function prints the name of the removed patient.
# The `remove_patient` function prompts the user to enter a specialization and patient name,
# and removes the patient from the queue for that specialization. 
# If the patient is not found in the queue, the function prints an error message.
# The main program runs in a loop, displaying a menu of options to the user 
# and calling the appropriate function based on their choice. 
# The program continues to run until the user chooses to end the program.
queue = [[] for i in range(20)]

def add_patient():
    spec = int(input("Enter specialization (1-20): "))
    if len(queue[spec-1]) >= 10:
        print("Sorry, this specialization is full.")
        return
    name = input("Enter patient name: ")
    status = int(input("Enter patient status (0=normal, 1=urgent, 2=super urgent): "))
    if status == 0:
        queue[spec-1].append((name, 0))
    elif status == 1:
        queue[spec-1].insert(0, (name, 1))
    elif status == 2:
        queue[spec-1].insert(0, (name, 2))
    else:
        print("Invalid status. Please enter 0 for normal, 1 for urgent, or 2 for super urgent.")

def print_patients():
    for i, patients in enumerate(queue):
        print(f"Specialization {i+1}:")
        sorted_patients = sorted(patients, key=lambda x: x[1], reverse=True)
        for patient, status in sorted_patients:
            print(f"Patient: {patient}")

def get_next_patient():
    spec = int(input("Enter specialization (1-20): "))
    if len(queue[spec-1]) == 0:
        print("No patients in this specialization.")
        return
    patient = queue[spec-1][0]
    queue[spec-1] = queue[spec-1][1:]
    print("Next patient:", patient)

def remove_patient():
    spec = int(input("Enter specialization (1-20): "))
    name = input("Enter patient name: ")
    if name not in queue[spec-1]:
        print("Patient not found.")
        return
    queue[spec-1].remove(name)
    print(name, "has been removed from the queue.")

while True:
    print("Program options:")
    print("1) Add new patient")
    print("2) Print all patients")
    print("3) Get next patient")
    print("4) Remove a leaving patient")
    print("5) End the program")
    
    choice = int(input("Enter your choice (from 1 to 5): "))
    
    if choice == 1:
        add_patient()
        
    elif choice == 2:
        print_patients()
        
    elif choice == 3:
        get_next_patient()
        
    elif choice == 4:
        remove_patient()
        
    elif choice == 5:
        break
        
    else:
        print("Invalid input. Please enter a number from 1 to 5.")
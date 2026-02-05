listdata=[]
def student_registration():
    student = {
        "id": int(input("please enter ID: ")),
        "name": input("please enter Name: ").title(),
        "address": input("please enter Address: ").title()
    }
    listdata.append(student)
    print("Student registered successfully")
    return listdata

def view_student_data():
        for student in listdata:
                print(student)

def search_student_record():
    search_id = int(input("please enter ID to search: "))

    for s in listdata:
        if s["id"] == search_id:
            print("ID:", s["id"])
            print("Name:", s["name"])
            print("Address:", s["address"])
            break

def dashbord():
    while True:
        print("\n----- STUDENT MENU -----")
        print("1. student registration")
        print("2. view student data")
        print("3. search student record")
        print("4. exit")

        choice = int(input("please enter your choice: "))

        if choice == 1:
            student_registration()

        elif choice == 2:
            view_student_data()

        elif choice == 3:
            search_student_record()

        elif choice == 4:
            print("Program exited")
            break

        else:
            print("Invalid choice")

dashbord()

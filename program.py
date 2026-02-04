listdata = []

while(True):
    print("\n----- STUDENT MENU -----")
    print("1. Register Student")
    print("2. Search Student")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student = {}
        student["id"] = int(input("please enter ID: "))
        student["name"] = input("please enter Name: ")
        student["address"] = input("please enter Adress: ")
        student["email"] = input("please enter Email: ")

        listdata.append(student)
        print("Student registered successfully")
        
    elif choice == 2:
        search_by_id = int(input("Enter ID to search: "))

        for s in listdata:
            if s["id"] == search_by_id:
                print("ID:", s["id"])
                print("Name:", s["name"])
                print("Address:", s["address"])
                print("Email:", s["email"])
                break


    elif choice == 3:
        print("Program exit")
        break

    else:
        print("Invalid")

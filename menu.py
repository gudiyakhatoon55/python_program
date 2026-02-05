def menu():
    while(True):
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
    
        choice=int(input("please enter any choice: "))

        return choice
    
def user_input(choice):
        a=int(input("please enter any number: "))
        b=int(input("please enter any number: "))

        if choice == 1:
                print(a+b)
        elif choice == 2:
                print(a-b)
        elif choice == 3:
                print(a*b)

choice = menu()
user_input(choice)

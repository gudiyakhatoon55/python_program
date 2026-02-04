a=int(input("please enter number: "))
b=int(input("please enter number: "))

def add(a,b):
    print(a+b)

def subtract(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def divide(a,b):
    print(a/b)


def menu():
    print("1. add ")
    print("2. subtract ")
    print("3. multiply ")
    print("4. divide ")

    option=int(input("please enter any option: "))
    return option

def dashbord():
    number=menu()
    if number==1:
        add(a,b)
    elif number==2:
        subtract(a,b)
    elif number==3:
        multiply(a,b)
    elif number==4:
        divide(a,b)

dashbord()
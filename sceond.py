name=input("pleas enter student name: ")

hindi=int(input("please entet any hindi marks: "))
english=int(input("please enter any english marsk: "))
maths=int(input("please enter any maths marks: "))
science=int(input("please enter any science marks: "))
computer=int(input("please enter any computer marks: "))

total=hindi+english+maths+science+computer
percentage=total/5
 
print("******Result******")
print("Name:",name)
print("Hindi marks:",hindi)
print("English marks:",english)
print("Maths marks:",maths)
print("Science marks:",science)
print("Computer marks:",computer)
print("Total marks:",total)
print("Percentage",percentage)

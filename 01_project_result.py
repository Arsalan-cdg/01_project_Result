name = input("Enter your name: ")
roll_no = int(input("Enter your Roll_No: "))
math = int(input("Enter your marks of math: "))
chemistry = int(input("Enter your marks of chemistry: "))
physics = int(input("Enter your marks of physics: "))
english = int(input("Enter your marks of english: "))
computer = int(input("Enter your marks of computer: "))
total_marks = math+chemistry+physics+english+computer
total_percent = (total_marks/500)*100
print("Name : ",name)
print("Roll_no : ",roll_no)
print(f"Percentage : {total_percent:.2f}")
if (total_percent > 90):
    print("Grade: A")
elif (total_percent > 80):
    print("Grade: B")
elif (total_percent > 70):
    print("Grade: C")
elif (total_percent > 60):
    print("Grade: D")
else :
    print("Grade: F")
if (math < 33 or chemistry < 33 or physics < 33 or english < 33 or computer < 33 ):
    print("Result : Fail")
else :
    print("Result : Pass")
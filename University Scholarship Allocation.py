
marks = float(input("Enter aggregate marks: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))

if marks >= 75 and attendance >= 75 and income <= 200000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")

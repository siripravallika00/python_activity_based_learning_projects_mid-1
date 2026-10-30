
attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details")
else:
    count = 0
    percentage = attended * 100 / total

    while percentage < 75:
        attended = attended + 1
        total = total + 1
        count = count + 1
        percentage = attended * 100 / total

    print("Attendance percentage =", percentage)
    print("Additional classes required =", count)

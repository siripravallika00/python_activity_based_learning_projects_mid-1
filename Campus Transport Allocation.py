students = int(input("Enter number of students: "))
capacity = int(input("Enter bus capacity: "))

if students < 0 or capacity <= 0:
    print("Invalid input")
elif students == 0:
    print("No buses required")
else:
    buses = 0
    remaining = students

    while remaining > 0:
        buses = buses + 1
        remaining = remaining - capacity

    print("Number of buses required =", buses)

    if remaining < 0:
        print("Seats available in last bus =", -remaining)
    else:
        print("All buses are full")

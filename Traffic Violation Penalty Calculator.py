
print("1. No helmet")
print("2. Overspeeding")
print("3. Signal jumping")

choice = int(input("Enter violation number: "))
repeat = input("Is this a repeat offence? (yes/no): ")

if choice == 1:
    fine = 500
elif choice == 2:
    fine = 1000
elif choice == 3:
    fine = 1500
else:
    fine = 0
    print("Invalid violation")

if fine > 0:
    if repeat == "yes":
        fine = fine * 2
        print("Repeat offence")
    elif repeat != "no":
        fine = 0
        print("Invalid repeat-offence input")

    if fine > 0:
        print("Traffic fine = Rs.", fine)

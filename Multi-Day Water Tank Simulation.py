
capacity = 1000
level = 500

days = int(input("Enter number of days: "))

if days <= 0:
    print("Invalid number of days")
else:
    for day in range(1, days + 1):
        print("Day", day)

        inflow = int(input("Enter water inflow: "))
        outflow = int(input("Enter water outflow: "))

        if inflow < 0 or outflow < 0:
            print("Invalid water quantity")
        else:
            level = level + inflow - outflow

            if level > capacity:
                print("Overflow detected")
                level = capacity
            elif level < 0:
                print("Water shortage detected")
                level = 0
            else:
                print("Water level is normal")

            print("Water level =", level, "litres")

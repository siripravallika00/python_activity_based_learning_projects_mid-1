
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

if price < 0 or quantity <= 0:
    print("Invalid input")
else:
    total = price * quantity

    if total >= 5000:
        discount = total * 0.15
    elif total >= 2000:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    print("Total amount =", total)
    print("Discount =", discount)
    print("Final bill =", final_bill)

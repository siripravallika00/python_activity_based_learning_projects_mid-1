
n = int(input("Enter number of rows: "))

if n <= 0:
    print("Enter a positive number")
elif n > 20:
    print("Enter a number up to 20")
else:
    for i in range(1, n + 1):

        for j in range(1, n - i + 1):
            print(" ", end="")

        for j in range(1, i + 1):
            print(j, end=" ")

        print()

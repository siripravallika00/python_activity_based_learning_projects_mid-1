
marks = [
    [80, 75, 90],
    [60, 70, 65],
    [95, 85, 90]
]

for i in range(3):
    total = 0

    for j in range(3):
        total = total + marks[i][j]

    average = total / 3

    print("Student", i + 1)
    print("Total marks =", total)
    print("Average marks =", average)

    if average >= 75:
        print("Performance: Good")
    else:
        print("Performance: Needs improvement")


key = "ABCDAB"
correct = 0
wrong = 0
unanswered = 0

for i in range(6):
    answer = input("Enter answer " + str(i + 1) + ": ")
    answer = answer.upper()

    if answer == "":
        unanswered = unanswered + 1
    elif answer == key[i]:
        correct = correct + 1
    else:
        wrong = wrong + 1

marks = correct * 2 - wrong

print("Correct answers =", correct)
print("Wrong answers =", wrong)
print("Unanswered =", unanswered)
print("Final marks =", marks)

attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))

classes_needed = 0

while attended / total < 0.75:
    attended = attended + 1
    total = total + 1
    classes_needed = classes_needed + 1

print("Additional classes needed =", classes_needed)
print("Attendance percentage =", attended / total * 100)
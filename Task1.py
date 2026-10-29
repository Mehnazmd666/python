marks_in_percentage = int(input("Enter marks in percentage: "))
attendance_percentage = int(input("Enter attendance percentage: "))
rank = float(input("Enter rank: "))
income = float(input("Enter income: "))
subjectwise_minimum_marks = int(input("Enter subject-wise minimum marks: "))
if marks_in_percentage >= 60 and attendance_percentage >= 75 and rank <= 1000 and income <= 500000 and subjectwise_minimum_marks >= 40:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
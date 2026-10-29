marks1 = int(input("Enter first exam marks: "))
marks2 = int(input("Enter second exam marks: "))

if marks2 > marks1:
    print("Performance improved")
elif marks2 < marks1:
    print("Performance decreased")
else:
    print("Performance remained the same")
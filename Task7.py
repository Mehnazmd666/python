prepared = int(input("Enter meals prepared: "))
served = int(input("Enter meals served: "))

waste = prepared - served

print("Meals wasted =", waste)

if waste > 0:
    percentage = waste / prepared * 100
    print("Waste percentage =", percentage)

    if percentage > 10:
        print("Food waste is high")
    else:
        print("Food waste is acceptable")
else:
    print("No food waste")
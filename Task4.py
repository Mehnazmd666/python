material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
machine = float(input("Enter machine cost: "))
sales = float(input("Enter sales amount: "))

total_cost = material + labour + machine
profit = sales - total_cost

print("Total cost =", total_cost)

if profit > 0:
    print("Profit =", profit)
elif profit < 0:
    print("Loss =", -profit)
else:
    print("No profit, no loss")
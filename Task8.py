balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount <= balance:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance =", balance)
else:
    print("Insufficient balance")
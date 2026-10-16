# Personal Expense Tracker

name = input("Enter your name: ")

expenses = []
n = int(input("How many expenses do you want to enter? "))

for i in range(n):
    expense = float(input("Enter expense amount: ₹"))
    expenses.append(expense)

total = sum(expenses)

print("\n--- EXPENSE REPORT ---")
print("Name:", name)
print("Total expenses:", len(expenses))
print("Total amount spent: ₹", total)

if total > 1000:
    print("Message: You spent more than ₹1000.")
else:
    print("Message: Your spending is within ₹1000.")

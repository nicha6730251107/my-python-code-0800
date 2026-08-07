prices = []
print("Enter prices of 6 items:")
for i in range(1, 7):
    price = int(input("Item " + str(i) + ": "))
    prices.append(price)

print()
budget = int(input("Enter total budget: "))
print()

current_total = 0
bought_items = []

for i in range(6):
    price = prices[i]
    if current_total + price <= budget:
        current_total = current_total + price
        bought_items.append(price)
        status = "buy"
    else:
        status = "cannot buy"
    
    print("Item", str(i + 1), "=", price, "->", status)
    print("Current total =", current_total)
    print()

remaining_budget = budget - current_total

print("Bought items:", bought_items)
print("Total spent:", current_total)
print("Remaining budget:", remaining_budget)
print("Choose conversion direction:")
print("1: THB to USD")
print("2: USD to THB")
choice = input("Enter choice (1 or 2): ")

rate = 35.5

if choice == "1":
    thb = float(input("Enter amount in THB: "))
    usd = thb / rate
    print(f"Result: {usd:.2f} USD")
    print(f"Formula used: USD = THB / {rate}")
elif choice == "2":
    usd = float(input("Enter amount in USD: "))
    thb = usd * rate
    print(f"Result: {thb:.2f} THB")
    print(f"Formula used: THB = USD * {rate}")
else:
    print("Invalid choice!")
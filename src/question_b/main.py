def get_bonus_pay_amount(sales):
    if not (0 <= sales <= 1999):
        return "Invalid arguments"
    rates = [(499, 0.05), (999, 0.06), (1499, 0.07), (1999, 0.08)]
    return next(sales * rate for limit, rate in rates if sales <= limit)

for test in [-1, 200, 600, 1000, 1500, 2000]:
    print(f"Sales: {test}, Bonus: {get_bonus_pay_amount(test)}")

while True:
    try:
        sales = int(input("Enter sales amount (0 to exit): "))
        if sales == 0:
            print("Goodbye!")
            break
        print("Bonus pay amount:", get_bonus_pay_amount(sales))
    except ValueError:
        print("Error: Please enter the right amount.")


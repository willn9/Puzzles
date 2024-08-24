# This function minimizes computations and copper :) (minimizes number of coins)
def change(amount):
    if amount == 8:
        return [3, 5]

    if amount < 8:
        return None

    amount_less_8 = amount - 8
    initial_five_cent_coins = amount_less_8 // 5
    remaining_amount = 8 + amount_less_8 % 5

    for i in range(remaining_amount // 5 + 1):
        for j in range(remaining_amount // 3 + 1):
            if 3 * j + 5 * i == remaining_amount:
                return [5] * (i+ initial_five_cent_coins) + [3] * j

    return None

try:
    amount = int(input("Enter an amount between 8 and 1000: "))
    if amount < 8 or amount > 1000:
        print("You did not enter a valid amount")
    else:
        result = change(amount)
        if result is not None:
            print(f"Change for {amount} in 5-cent and 3-cent coins: {result}")
        else:
            print(f"No solution found for {amount}")
except ValueError:
    print("You did not enter a valid amount!")

#This code will find number of 7-cent and 5-cent coins for any amount between 24 and 1000
#The goals are to minimize computations and use minimum number of coins
def change(amount):
    if amount == 24:
        return [5, 5, 7, 7]

    if amount < 24:
        return None

    amount_less_24 = amount - 24
    initial_seven_cent_coins = amount_less_24 // 7
    remaining_amount = 24 + amount_less_24 % 7

    for i in range(remaining_amount // 7 + 1):
        for j in range(remaining_amount // 5 + 1):
            if 7 * i + 5 * j == remaining_amount:
                return [7] * (i + initial_seven_cent_coins) + [5] * j

    return None

try:
    amount = int(input("Enter an amount between 24 and 1000: "))
    if amount < 24 or amount > 1000:
        print("You did not enter a valid amount")
    else:
        result = change(amount)
        if result is not None:
            print(f"Change for {amount}: {result}")
        else:
            print(f"No solution found for {amount}")
except ValueError:
    print("You did not enter a valid amount!")

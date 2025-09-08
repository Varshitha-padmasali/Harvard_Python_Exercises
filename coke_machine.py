# implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
# accepts coins of 5, 10, or 25 cents only.
# Continues asking for coins until the total reaches or exceeds 50 cents.
# Rejects invalid coins (e.g., 3, 7, 100).
# Tells the user how much is still due after each valid coin.
# At the end, outputs how much change the user is owed.
amount_due=50
while amount_due>0:
    print(f"Amount Due: {amount_due}")
    coin=int(input("Insert Coin: "))
    if coin in [5,10,25]:
        amount_due=amount_due-coin
change=abs(amount_due)
print(f"Change Owed: {change}")



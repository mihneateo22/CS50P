coke_price = 50
print(f"Amount Due: {coke_price}")
while(coke_price > 0):
    coin_amount = int(input("Insert Coin: "))
    match coin_amount:
        case 5 | 10 | 25:
            coke_price = coke_price - coin_amount
            if coke_price <= 0:
                print(f"Change Owed: {abs(coke_price)}")
            else:
                print(f"Amount Due: {coke_price}")
        case _:
            print(f"Amount Due: {coke_price}")
def final_deposit_amount(*interests, amount=1000):
    for interest in interests:
        amount *= 1 + interest / 100
    return round(amount, 2)


# rates = [int(rate) for rate in input().split()]
# print(final_deposit_amount(*rates))

def calculate(hand):
    result = 0
    for card in hand:
        result += card_values[card]
    return result / 6


global card_values
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
               'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

cards = list()
for i in range(6):
    cards.append(input())
print(calculate(cards))

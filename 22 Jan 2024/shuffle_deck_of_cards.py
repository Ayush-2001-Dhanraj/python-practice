import random, itertools

deck = list(itertools.product(range(1, 14), ["Spades", "Club", "Hearts", "Diamonds"]))

# print(deck)

random.shuffle(deck)

# print(deck)
print(deck[:5])
# Bingo card 6kyu
# After yet another dispute on their game the Bingo Association decides to change course and automate the game.
# Can you help the association by writing a method to create a random Bingo card?

# Bingo Cards
# A Bingo card contains 24 unique and random numbers according to this scheme:

# 5 numbers from the B column in the range 1 to 15        B 5numbers  1-15
# 5 numbers from the I column in the range 16 to 30       I 5numbers  16-30
# 4 numbers from the N column in the range 31 to 45       N 4numbers  31-45
# 5 numbers from the G column in the range 46 to 60       G 5numbers  46-60
# 5 numbers from the O column in the range 61 to 75       O 5numbers  61-75
# Task
# Write the function get_card(). The card must be returned as an array of Bingo style numbers:

# [ 'B14', 'B12', 'B5', 'B6', 'B3', 'I28', 'I27', ... ]
# The numbers must be in the order of their column: B, I, N, G, O. Within the columns the order of the numbers is random.
import random

def get_bingo_card():
    result = []
    for b in random.sample(range(1, 16), 5):
        result.append(f"B{b}")
    for i in random.sample(range(16, 31), 5):
        result.append(f"I{i}")
    for n in random.sample(range(31, 46), 4):
        result.append(f"N{n}")
    for g in random.sample(range(46, 61), 5):
        result.append(f"G{g}")
    for o in random.sample(range(61, 76), 5):
        result.append(f"O{o}")
    
    return result

print(get_bingo_card())

      

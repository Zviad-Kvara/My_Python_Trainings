# Dictionary of factors 6kyu

# The objective of this Kata is to write a function that creates a dictionary of factors for a range of numbers.
# The key for each list in the dictionary should be the number. The list associated with each key should possess the factors for 
# the number.
# If a number possesses no factors (only 1 and the number itself), the list for the key should be ['None']
# The function possesses two arguments (n and m). Where n is the starting number and m is the ending number.
# For example: All factors for 2 (n) through to 6 (m) with the number being the key in the dictionary:
# {2: ['None'], 3: ['None'], 4: [2], 5: ['None'], 6: [2, 3]}

def factors_range(n, m):
    result = {}
    for key in range(n, m + 1):         # 2, 3,  4,  5,   6
        if key < 4:
            result[key] = ['None']

        for value in range(2, key):     #    2   23  234  2345
            if key % value == 0:
                result.setdefault(key, []).append(value)
        if key not in result:
            result[key] = ['None'] 
             
    return result


print(factors_range(2, 6))            # {2: ['None'], 3: ['None'], 4: [2], 5: ['None'], 6: [2, 3]}


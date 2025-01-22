# Dictionary form two lists 7kyu

# There are two lists, possibly of different lengths. The first one consists of keys, the second one consists of values. 
# Write a function that returns a dictionary created from keys and values. If there are not enough values, 
# the rest of keys should have a None. If there not enough keys, just ignore the rest of values.
# Example 1:
# keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3]
# createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3, 'd': None}
# Example 2:
# keys = ['a', 'b', 'c']
# values = [1, 2, 3, 4]
# createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3}
def createDict(keys, values):
    result = {}
    for index, key in enumerate(keys):     
        if index < len(values):
            result[key] = values[index]
        else:
            result[key] = None
            
    return result

def createDict(keys, values):
    return {keys[index]: (values[index] if index<len(values) else None) for index,key in enumerate(keys)}

print(createDict(['a', 'b', 'c', 'd'],[1, 2, 3]))   # {'a': 1, 'b': 2, 'c': 3, 'd': None}
print(createDict(['a', 'b', 'c'],[1, 2, 3, 4]))   # {'a': 1, 'b': 2, 'c': 3}
print(createDict(['f', 'R'],[5, 7]))   # {'f': 5, 'R': 7}

def createDict(keys, values):  
    while len(keys) > len(values):
        values.append(None)
    dic = dict(zip(keys, values))
    return dic

print(createDict(['a', 'b', 'c', 'd', 'f'],[1, 2, 3]))   # {'f': 5, 'R': 7}
# print(createDict(['a', 'b', 'c'],[1, 2, 3, 4]))   # {'f': 5, 'R': 7}
# print(createDict(['f', 'R'],[5, 7]))   # {'f': 5, 'R': 7}

# def create_dict(keys, values):
#     return {keys[x]:(values[x] if x<len(values) else None) for x,y in enumerate(keys)}

# print(createDict(['a', 'b', 'c', 'd', 'f'],[1, 2, 3]))   # {'f': 5, 'R': 7}
# print(createDict(['a', 'b', 'c'],[1, 2, 3, 4]))   # {'f': 5, 'R': 7}
# print(createDict(['f', 'R'],[5, 7]))   # {'f': 5, 'R': 7}

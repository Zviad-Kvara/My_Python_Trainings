# Sorting dictionaries 7kyu
# Python dictionaries are inherently unsorted. So what do you do if you need to sort the contents of a dictionary?
# Create a function that returns a sorted list of (key, value) tuples.
# The list must be sorted by the value and be sorted largest to smallest.

# Examples
# sort_dict({3:1, 2:2, 1:3}) == [(1,3), (2,2), (3,1)]
# sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)]
def sort_dict(d):
    return sorted(d.items(), key=lambda item: item[1], reverse=True)

print(sort_dict({3: 1, 2: 2, 1: 3}))      # [(1,3), (2,2), (3,1)]
print(sort_dict({1:2, 2:4, 3:6}))         # [(3,6), (2,4), (1,2)]
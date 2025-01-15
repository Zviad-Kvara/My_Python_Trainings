# You've just discovered a square (NxN) field and you notice a warning sign. The sign states that there's a 
# single bomb in the 2D grid-like field in front of you.

# Write a function that accepts a 2D array, and returns the location of the mine. 
# The mine is represented as  1 in the 2D array. Areas in the 2D array that are not the mine will 
# be represented as 0s.

# The location returned should be an array where the first element 
# is the row index, and the second element is the column index of the bomb location (both should be 0 based). 
# All 2D arrays passed into your function will be square (NxN), and there will only be one mine in the array.

# Examples:
# mineLocation( [ [1, 0, 0], [0, 0, 0], [0, 0, 0] ] ) => returns [0, 0]
# mineLocation( [ [0, 0, 0], [0, 1, 0], [0, 0, 0] ] ) => returns [1, 1]
# mineLocation( [ [0, 0, 0], [0, 0, 0], [0, 1, 0] ] ) => returns [2, 1]
def mine_location(field):
   for raw, i in enumerate(field):
      for column, bomb in enumerate(i):
        if bomb == 1:
            return [raw, column]
            
            

            
print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))   # => returns [0, 0]
# print(mine_location([ [0, 0, 0], [0, 1, 0], [0, 0, 0] ])) # => returns [1, 1]
# print(mine_location([ [0, 0, 0], [0, 0, 0], [0, 1, 0] ])) # => returns [2, 1]
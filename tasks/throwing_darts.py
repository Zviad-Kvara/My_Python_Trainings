# Throwing darts 6kyu

# You've just recently been hired to calculate scores for a Dart Board game!

# Scoring specifications:

# 0 points - radius above 10                                 x > 10 = 0pts
# 5 points - radius between 5 and 10 inclusive               5 < x < 10 = 5pts
# 10 points - radius less than 5                             x < 5 = 10pts
# If all radii are less than 5, award 100 BONUS POINTS!

# Write a function that accepts an array of radii (can be integers and/or floats), and returns a total score using the above 
# specification.

# An empty array should return 0.

# Examples:
# scoreThrows( [1, 5, 11] )    =>  15
# scoreThrows( [15, 20, 30] )  =>  0
# scoreThrows( [1, 2, 3, 4] )  =>  140
def score_throws(radii):
    if radii == []:
        return 0

    less_than_five = True
    sum = 0
    for i in radii:
        if i > 10:
            sum += 0
        if 5 <= i <= 10:
            sum += 5
        if i < 5:
            sum += 10
        if i >= 5:
            less_than_five = False

    if less_than_five:
        sum += 100
        
    return sum

print(score_throws([1, 2, 3, 4]))    # 140   
print(score_throws([1, 5, 11]))      # 15
print(score_throws([15, 20, 30]))    # 0
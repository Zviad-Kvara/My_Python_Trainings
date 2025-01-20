# twisted sum 6kuy
# Find the sum of the digits of all the numbers from 1 to N (both ends included).
# Examples
# # N = 4
# 1 + 2 + 3 + 4 = 10

# # N = 10
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46

# # N = 12
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51
def compute_sum(n):
    result = 0
    for i in range(n + 1):
        if i > 9:
            digits = [int(d) for d in str(i)]
            result += sum(digits)
        if i <= 9:
            result += i

    return result   
    
    
            
print(compute_sum(12))   
print(compute_sum(10))       
print(compute_sum(4))

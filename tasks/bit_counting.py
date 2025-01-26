# Bit Counting
# leve: 6kyu

# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the 
# binary representation of that number. You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
def count_bits(n):
    remainders = []  
    while n > 0:      
        remainders.append(n % 2)  
        n = n // 2     
        
    return sum(remainders)
                                 # RETURN VALUES                
print(count_bits(4))             # 1
print(count_bits(1234))          # 5
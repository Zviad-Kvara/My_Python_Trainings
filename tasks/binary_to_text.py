# binary to text 6kyu

# Write a function that takes in a binary string and returns the equivalent decoded text (the text is ASCII encoded).

# Each 8 bits on the binary string represent 1 character on the ASCII table.

# The input string will always be a valid binary string.

# Characters can be in the range from "00000000" to "11111111" (inclusive)

# Note: In the case of an empty binary string your function should return an empty string.
def binary_to_string(binary):
    if not binary:
        return ''
    
    result = ''                                   
    for i in range(0, len(binary), 8):               # "01001000 01100101 01101100 01101100 01101111"
        chunks = binary[i : i + 8]
        reversed_chunks = chunks[::-1]               # "00010010 10100110 00110110 00110110 11110110"
        decimal = 0
        for index,j in enumerate(reversed_chunks):
            decimal += int(j) * (2 ** index)          # 72 101 108 108 111

        result += chr(decimal)
    
    return result
print(binary_to_string("0100100001100101011011000110110001101111"))     # 'Hello'
print(binary_to_string("00110001001100000011000100110001"))           # '1011'




# Find the missing letter
# 6kyu
# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at 
# least 2. The array will always contain letters in only one case.

# Example:
# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'
# (Use the English alphabet with 26 letters!)

def find_missing_letter(chars):
   for index,char in enumerate(chars[:-1]):
        if ord(chars[index + 1]) - ord(char) > 1:
            return  chr(ord(char) + 1)
            
print(find_missing_letter(['a','b','d'])) # 97 98 100   # 'c'  
print(find_missing_letter(['a','d']))                   # 'b'
print(find_missing_letter(['O','Q','R','S']))           # 'P'
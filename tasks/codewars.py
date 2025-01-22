# CODEWARS 1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

# def accum(str):
#     chars = []
#     for i in range(len(str)):
#         parts = (str[i] * (i + 1)).capitalize()
#         chars.append(parts)
#         print(chars)
#     print(chars)

# accum("abcd")

# CODEWARS 2  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Given an array of integers, return a new array with each value doubled.
# For example: [1, 2, 3] --> [2, 4, 6]

# def double(x):
#     r = []
#     for i in x:
#          r.append(i * 2)
#     return r

# print(double([1, 2, 3]))

# CODEWARS 3 !!!!!!! >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Check to see if a string has the same amount of 'x's and 'o's.The method must return a boolean and be case insensitive. The string 
# can contain any char.

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

# def XO(str):
#         if str.count("o") == str.count("x"):
#             return True
#         elif "o" not in str and "x" not in str:
#             return True
#         else:
#             return False


# print(XO("ooxx"))          # true
# print(XO("xooxx"))         # false
# print(XO("ooxXm"))         # true
# print(XO("zpzpzpp"))       # true
# print(XO("zzoo"))          # false

# CODEWARS 4 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 9**2 is 81 and 1**2 is 1. (81-1-1-81)
# Example #2: An input of 765 should return 493625 because 7**2 is 49, 6**2 is 36, and 5**2 is 25. (49-36-25)
# Note: The function accepts an integer and returns an integer.

# def square_digits(num):
#             r = []
#             for i in str(num):
#                     r.append(int(i) ** 2)
#                     result = int("".join(map(str, r)))
#             return result
                    
# print(square_digits(9119))
# print(square_digits(765))

# CODEWARS 5 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either 
# entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes 
# the array as an argument and returns this "outlier" N.
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)
# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

# def find_outlier(integers):
#             even = []
#             odd = []
#             for i in integers:
#                     if i % 2 == 0:
#                             even.append(i)
#                     else:
#                             odd.append(i)

#             if len(even) > 1:
#                    return odd[0]
                    
#             elif len(odd) > 1:
#                     return even[0]
                 
                                
# print(find_outlier([2, 4, 11, 36]))
# print(find_outlier([160, 3, -21]))

# def find_outlier(lst):
#   # [ 160, 3, -21] , mods = [0, 1, 1]
#   # [2, 4 , 36, 11] , mods = [0,0,0,1]

#   mods = [ i % 2 for i in lst]
#   return lst[mods.index(0)] if sum(mods) > 1 else lst[mods.index(1)]
 


# print(find_outlier([2, 4, 11, 36]))
# print(find_outlier([160, 3, -21]))

# CODEWARS 6 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 89 --> 8¹ + 9² = 89 * 1 
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51 / 2360688/46288 = k=51

# Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised 
# to consecutive powers starting from p is equal to k * n.

# In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that :
# abcd --> (a**p + b**p+1 + c**p+2 + d**p+3 +...)= n*k
# If it is the case we will return k, if not return -1.
# Note: n and p will always be strictly positive integers.
# n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1
# n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k
# n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
# n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# n = a,b, a**1 + b**2 = n * k, 

# def dig_pow(n, p):   
#     num = []         
#     for i in str(n):
#         if i == ".":
#             continue
#         num.append(int(i) ** p)
#         p += 1
        
#     digit = sum(num)    
#     k = digit // n       

#     if digit == n * k:  
#         return int(k)   
#     else:
#         return -1
    
# print(dig_pow(1,1))
# print(dig_pow(3263,3))
# print(dig_pow(3263.10819218804, 1))  
# print(dig_pow(89, 1))
# print(dig_pow(695, 2))
# print(dig_pow(46288, 3))

# CODEWARS 7 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more 
# letters reversed. Strings passed in will consist of only letters and spaces. 
# Spaces will be  included only when more than one word is present.
# Examples:
# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"

# def spin_words(sentence):             
#     words =  sentence.split()
    
#     for count, s in enumerate(words):   
#         if len(words[count]) >= 5:      
#              words[count] = s[::-1]

#     return " ".join(words)
    
    
    
# print(spin_words("Hey fellow warriors"))
# print(spin_words("This is a test"))
# print(spin_words("This is another test"))
    
# CODEWARS 8 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of
# that number. You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

# def count_bits(n):
#     remainders = []  

#     while n > 0:      
#         remainders.append(n % 2)  
#         n = n // 2     
        
#     return sum(remainders)


# print(count_bits(4))
# print(count_bits(1234))

# Codewars 9  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# you have to write a simple Morse code decoder.
# The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded 
# as ·− . The Morse code is case-insensitive.When the message is written in Morse code, a single space is used to 
# separate the character codes and 3 spaces are used to separate words.For example, the message HEY JUDE in Morse 
# code is ···· · −·−−   ·−−− ··− −·· ·.

# NOTE: Extra spaces before or after the code have no meaning and should be ignored.

# there are some special service codes, the most notorious of those is the 
# signal SOS, that is coded as ···−−−···. These special codes are treated as 
# single special characters, and usually are transmitted as separate words.

# Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

# For example:
#decode_morse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"

# NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

# The Morse code table is preloaded for you as a dictionary, feel free to use it:

# Coffeescript/C++/Go/JavaScript/Julia/PHP/Python/Ruby/TypeScript: MORSE_CODE['.--']
# C#: MorseCode.Get(".--") (returns string)
# F#: MorseCode.get ".--" (returns string)
# Elixir: @morse_codes variable (from use MorseCode.Constants). Ignore the unused variable warning for morse_codes because it's no 
# longer used and kept only for old solutions.
# Elm: MorseCodes.get : Dict String String
# Haskell: morseCodes ! ".--" (Codes are in a Map String String)
# Java: MorseCode.get(".--")
# Kotlin: MorseCode[".--"] ?: "" or MorseCode.getOrDefault(".--", "")
# Racket: morse-code (a hash table)
# Rust: MORSE_CODE
# Scala: morseCodes(".--")
# Swift: MorseCode[".--"] ?? "" or MorseCode[".--", default: ""]
# C: provides parallel arrays, i.e. morse[2] == "-.-" for ascii[2] == "C"
# NASM: a table of pointers to the morsecodes, and a corresponding list of ascii symbols

# All the test strings would contain valid Morse code, so you may skip checking for errors and exceptions. In C#, tests will fail if 
# the solution code throws an exception, please keep that in mind. This is mostly because otherwise the engine would simply ignore the 
# tests, resulting in a "valid" solution.

# from morse_code import MORSE_CODE

# def decode_morse(morse_code):
#     words = morse_code.split("   ")
#     decoded = []        
#     for word in words:
#         if word in MORSE_CODE:
#                decoded.append(MORSE_CODE[word])
#                continue 
#         temp_words = []
#         characters = word.split(" ")  
#         for char in characters:
#                     if char:
#                         temp_words.append(MORSE_CODE[char])
                
#         joined_word = "".join(temp_words) 
#         decoded.append(joined_word)       
                    
                        
#     sentence = " ".join(decoded)
#     result = sentence.strip()
#     return result
     

        
# print(decode_morse('   ...---...   .... . -.--   .--- ..- -.. .')) # --> HEY   JUDE
# print(decode_morse('  .  '))
# print(decode_morse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '))


# Codewars 10 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character 
# appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore 
# capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())" 
# "(( @"     =>  "))((" 

# Notes
# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" 
# is the expected result, not the input!

# def duplicate_encode(word):
#             word = word.lower()
#             characters = []

#             for char in word:
#                 if word.count(char) > 1:
#                     characters.append(")")
#                 else:
#                     characters.append("(")
            
#             return "".join(characters)

# print(duplicate_encode("(( @"))            
# print(duplicate_encode("Success"))
# print(duplicate_encode("recede"))
# print(duplicate_encode("din"))
# print(duplicate_encode("dinnd"))

# Codewars 11 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the 
# same value next to each other and preserving the original order of elements.

# For example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

# def unique_in_order(sequence):
#         result = []
#         previous = None
#         for char in sequence:
#                 if previous != char:
#                         result.append(char)
#                         previous = char
#         return result
                        
# print(unique_in_order('AASSDA'))
# print(unique_in_order([1, 2, 2, 3, 3]))
# print(unique_in_order('AAAABBBCCDAABBB'))
# print(unique_in_order('AAAABBBCCDAABBB'))

# Codewars 12 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, 
# with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements 
# in b are the elements in a squared, regardless of the order.

# Examples
# Valid arrays
# a = [121, 144, 19, 161, 19, 144, 19, 11]  
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 
# 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

# a = [121, 144, 19, 161, 19, 144, 19, 11] 
# b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# Invalid arrays
# If, for example, we change the first number to something else, comp is not returning true anymore:

# a = [121, 144, 19, 161, 19, 144, 19, 11]  
# b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
# comp(a,b) returns false because in b 132 is not the square of any number of a.

# a = [121, 144, 19, 161, 19, 144, 19, 11]  
# b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
# comp(a,b) returns false because in b 36100 is not the square of any number of a.

# Remarks
# a or b might be [] or {} (all languages except R, Shell).
# a or b might be nil or null or None or nothing (except in C++, COBOL, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, 
# Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift).
# If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.

# def comp(arr1, arr2):
#         if arr1 is None or arr2 is None:
#                 return False
        
#         squared_arr = []
#         for num in arr1:
#                 squared_arr.append(num**2)

#         if sorted(squared_arr) == sorted(arr2):
#                 return True
#         else:
#                 return False
        
# print(comp([2, 2, 3], [4, 9, 4]))
# print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))
# print(comp( [121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))
# print(comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]))
# print(comp(None, [2, 2, 3]))
# print(comp(None, None))

# CODEWARS 13 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Which are in?
# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of 
# strings of a2.

# Example 1:
# a1 = ["arp", "live", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

#returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []

# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
# In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
# Beware: In some languages r must be without duplicates.

# def in_array(array1, array2):
#     result = []
#     for compare_word in array1:
#         for word in array2:
#             if compare_word in word and not compare_word in result:
#                 result.append(compare_word)
#                 break

#     return sorted(result)  

# print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
# print(in_array(["tarp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))

# CODEWARS 14 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Convert string to camel case
# Complete the function so that it converts dash/underscore delimited words into camel casing. The first word within the output 
# should be capitalized only if the original word was capitalized, The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

# def to_camel_case(text):
#     words = text.replace("-"," ").replace("_", " ").split(" ") 
     
#     sentence = [words[0]]    
    
#     for word in words[1:]:   
#         sentence.append(word.title())  
    
#     return "".join(sentence) 

# print(to_camel_case(""))   
# print(to_camel_case("the-stealth-warrior"))
# print(to_camel_case("The_Stealth_Warrior"))
# print(to_camel_case("The_Stealth-Warrior"))

# CODEWARS 15 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# def solution(s):
#     words = []
#     start_index = 0

#     for index, char in enumerate(s):
#         if char.isupper():
#             words.append(s[start_index:index])
#             start_index = index
#     words.append(s[start_index:])
    
#     return " ".join(words)

# print(solution("camelCasing"))
# print(solution("identifier"))
# print(solution(""))

# CODEWARS 16 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Gap in Primes >>> 5Kyu
# The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. 
# Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

# A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes 
# (see: http://mathworld.wolfram.com/PrimeGaps.html).

# We will write a function gap with parameters:

# g (integer >= 2) which indicates the gap we are looking for

# m (integer > 2) which gives the start of the search (m inclusive)

# n (integer >= m) which gives the end of the search (n inclusive)

# In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.

# So this function should return the first pair of two prime numbers spaced with a gap of g between the limits m, n if these numbers 
# exist otherwise `nil or null or None or Nothing.

# In such a case (no pair of prime numbers with a gap of `g`)
# In C: return [0, 0]
# In C++, Lua, COBOL: return `{0, 0}`. 
# In F#: return `[||]`. 
# In Kotlin, Dart and Prolog: return `[]`.
# In Pascal: return Type TGap (0, 0).
# Examples:
# - gap(2, 5, 7) --> [5, 7] or (5, 7) or {5, 7}

# gap(2, 5, 5) --> nil. In C++ {0, 0}. In F# [||]. In Kotlin, Dart and Prolog return []`

# gap(4, 130, 200) --> [163, 167] or (163, 167) or {163, 167}

# ([193, 197] is also such a 4-gap primes between 130 and 200 but it's not the first pair)

# gap(6,100,110) --> nil or {0, 0} or ... : between 100 and 110 we have 101, 103, 107, 109 but 101-107is not a 6-gap because there is 
# 103in between and 103-109is not a 6-gap because there is 107in between.

# You can see more examples of return in Sample Tests.

# Note for Go
# For Go: nil slice is expected when there are no gap between m and n. Example: gap(11,30000,100000) --> nil
# Ref
# https://en.wikipedia.org/wiki/Prime_gap

# def gap(g, m, n):
#     prime_nums = []        
#     for num in range(m, n + 1):    
#         if num > 1:
#             for i in range(2, num):    
#                 if num % i == 0:
#                     break
#             else:
#                 prime_nums.append(num)  
    
#     for index in range(len(prime_nums) - 1):    
#         if prime_nums[index + 1] - prime_nums[index] == g:
#             return [prime_nums[index],prime_nums[index+1]]
    
    
# print(gap(6,100,110))           #  None           
# print(gap(2, 2, 10))            # [3, 5]
# print(gap(2, 5, 5))             # None
# print(gap(4, 130, 200))         # >> [163, 167]
# print(gap(2,410657,510657))     


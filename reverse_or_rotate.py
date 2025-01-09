# Reverse or rotate?  <6kyu, Algorithms Strings>

# The input is a string of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of 
# size sz (ignore the last chunk if its size is less than sz).

# If the sum of a chunk's digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. 
# Put together these modified chunks and return the result as a string.

# If sz is <= 0 or if str == "" return ""
# if sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".

# Examples:
# ("123456 987654", 6) --> "234561 876549"
# ("123456 987653", 6) --> "234561 356789"
# ("6644 3875", 4) --> "4466 8753"
# ("66443875", 8) --> "64438756"
# ("66443876 9", 8) --> "67834466"
# ("12345677 9", 8) --> "23456771"
# ("", 8) --> ""
# ("123456779", 0) --> "" 
# ("5630 0065 5734 4694 85", 4) --> "0365 0650 7345 6944"

# Example of a string rotated to the left by one position:
# s = "123456" gives "234561".

def rev_rot(string, sz):
    if sz <= 0 or string == "":         
        return "" 

    result = []                                 
    for i in range(0, len(string), sz):      
        chunk = string[i: i+sz]              
    
        if sz > len(chunk):                  
            continue
        
        total = 0                   
        for num in chunk:
            total += int(num)

        if total % 2 == 0:
            result.append(chunk[::-1])
        else:
            result.append(chunk[1:] + chunk[0])

    return "".join(result)

print(rev_rot("563000655734469485", 4))  # "0365 0650 7345 6944"
# print(rev_rot("664438769", 8))           # "67834466"
# print(rev_rot("123456779", 8))           # --> "23456771"
# print(rev_rot("", 8))                    # --> ""
# print(rev_rot("563000655734469485", 4))  # "0365 0650 7345 6944"



 

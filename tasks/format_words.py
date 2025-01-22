# format words into sentence 6kyu

# Complete the method so that it formats the words into a single comma separated value. The last word should 
# be separated by the word 'and' instead of a comma. The method takes in an array of strings and returns a 
# single formatted string.

# Note:

# Empty string values should be ignored.
# Empty arrays or null/nil/None values being passed into the method should result in an empty string being 
# returned.
# Example: (Input --> output)
# ['ninja', 'samurai', 'ronin'] --> "ninja, samurai and ronin"
# ['ninja', '', 'ronin'] --> "ninja and ronin"
# [] -->""
# formatWords([]) should return "": [] should equal ''
def format_words(words):
    if not words: return ""
    words = [word for word in words if word]
    
    number_of_words = len(words)
    if number_of_words <= 2:
        joiner = ' and ' if number_of_words == 2 else ''
        return joiner.join(words)
    
    return ", ".join(words[:-1]) + " and " + words[-1]
    
    
     
print(format_words(['one', 'two', 'three', 'four']))
print(format_words(['one', 'two']))
print(format_words(['one']))
print(format_words([]))

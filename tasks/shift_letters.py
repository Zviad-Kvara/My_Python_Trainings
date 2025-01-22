# translate word "hello" with CIPHER text, where letters shifted by 3
def cipher(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted = "defghijklmnopqrstuvwxyzabc"

    table = str.maketrans(alphabet, shifted)

    return text.translate(table)
print(cipher("hello"))
def atbash(text):
    alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    reversed_alphabet = "zyvüutşsrpöonmlkjiıhğgfedçcba"
    result = ""

    for char in text.lower():
        if char.isalpha():
            index = alphabet.index(char)
            result += reversed_alphabet[index]
        else:
            result += char

    return result

pt = input("Plain Text: ")
ct = atbash(pt)
print("Cipher Text:", ct)

def atbash_decrypt(ciphertext):
    alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    reversed_alphabet = "zyvüutşsrpöonmlkjiıhğgfedçcba"
    result = ""

    for char in ciphertext.lower():
        if char.isalpha():
            index = reversed_alphabet.index(char)
            result += alphabet[index]
        else:
            result += char

    return result

ct = input("Cipher Text: ")
pt = atbash_decrypt(ct)
print("Plain Text:", pt)

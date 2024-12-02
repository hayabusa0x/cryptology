def caesar_encrypt(text, shift, direction):
    alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
    encrypted_text = ""

    for char in text.lower():
        if char.isalpha():
            index = alphabet.index(char)
            if direction == "forward":
                index = (index + shift) % 29
            elif direction == "back":
                index = (index - shift) % 29
            encrypted_text += alphabet[index]
        else:
            encrypted_text += char

    return encrypted_text

pt = input("Plain Text: ")
scroll_number = int(input("Number of scrolls:  "))
scroll = input("select scroll direction (forward/back): ")

ct = caesar_encrypt(pt, scroll_number, scroll)
print("Cipher Text:", ct)

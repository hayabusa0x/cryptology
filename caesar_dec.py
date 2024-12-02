alphabet = 'abcçdefgğhıijklmnoöprsştuüvyz'

def shift_char(char, shift_amount):
    if char in alphabet:
        original_index = alphabet.index(char)
        new_index = (original_index + shift_amount) % len(alphabet)
        return alphabet[new_index]
    else:
        return char

def shift_text(text, shift_amount):
    shifted_text = ''.join(shift_char(char, shift_amount) for char in text)
    return shifted_text

def main():
    encrypted_text = input("Cipher Text: ")

    results = []

    for i in range(1, 6):
        shifted_text_forward = shift_text(encrypted_text, i)
        results.append(f'{i} scroll forward times: {shifted_text_forward}')
        print(f'{i} scroll forward times: {shifted_text_forward}')
        
        shifted_text_backward = shift_text(encrypted_text, -i)
        results.append(f'{i} scroll back times: {shifted_text_backward}')
        print(f'{i} scroll back times: {shifted_text_backward}')

    with open('shifted_results.txt', 'w', encoding='utf-8') as file:
        for result in results:
            file.write(result + '\n')

if __name__ == "__main__":
    main()

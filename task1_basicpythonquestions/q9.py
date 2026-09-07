def caesar_cipher(text, shift):
    result = ""

    for character in text:
        if character.isalpha():
            start = ord('A') if character.isupper() else ord('a')
            result += chr((ord(character) - start + shift) % 26 + start)
        else:
            result += character

    return result


text = input("Enter a string: ")
shift = int(input("Enter the shift value: "))

encrypted_text = caesar_cipher(text, shift)

print("Encrypted string:", encrypted_text)
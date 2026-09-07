def luhn_check(card_number):
    card_number = card_number.replace(" ", "").replace("-", "")

    if not card_number.isdigit():
        return False

    total = 0
    reverse_digits = card_number[::-1]

    for i in range(len(reverse_digits)):
        digit = int(reverse_digits[i])

        if i % 2 == 1:
            digit = digit * 2

            if digit > 9:
                digit = digit - 9

        total += digit

    return total % 10 == 0


card_number = input("Enter credit card number: ")

if luhn_check(card_number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")
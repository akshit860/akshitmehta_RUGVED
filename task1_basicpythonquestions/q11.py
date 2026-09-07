def count_letters(text):
    count = 0

    for character in text:
        if character.isalpha():
            count += 1

    return count


def count_words(text):
    return len(text.split())


def count_sentences(text):
    count = 0

    for character in text:
        if character in ".!?":
            count += 1

    return count


text = input("Enter a text: ")

letters = count_letters(text)
words = count_words(text)
sentences = count_sentences(text)

if words == 0:
    print("No words found.")
elif sentences == 0:
    print("No sentences found.")
else:
    L = (letters / words) * 100
    S = (sentences / words) * 100

    grade = 0.0588 * L - 0.296 * S - 15.8

    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print("Grade", round(grade))
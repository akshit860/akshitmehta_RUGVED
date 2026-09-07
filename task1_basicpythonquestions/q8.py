string = input("Enter a string: ")
n = int(input("Enter the number of characters in each part: "))

if len(string) % n != 0:
    print("Error: String cannot be divided into equal parts.")
else:
    parts = []

    for i in range(0, len(string), n):
        parts.append(string[i:i + n])

    if len(set(parts)) != 1:
        print("Error: All parts do not have the same sequence.")
    else:
        print("Parts:")
        for part in parts:
            print(part)
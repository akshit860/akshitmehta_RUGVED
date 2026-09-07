def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if are_anagrams(str1, str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
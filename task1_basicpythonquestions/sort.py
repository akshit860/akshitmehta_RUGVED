def main():
    st=input("Enter a string \n")
    sort=sorted(st)
    count = {}
    for char in sort:
        count[char] = count.get(char, 0) + 1
    for char, counts in count.items():
        print(f"{char} count is {counts}")
main()
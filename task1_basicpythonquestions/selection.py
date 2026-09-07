def main():
    n = input("give a string: \n")
    print(sort(n))


def sort(n):
    n = list(n)
    for i in range(len(n)):
        min_ = i
        for j in range(i + 1, len(n)):
            if n[j] < n[min_]:
                min_ = j
        n[i], n[min_] = n[min_], n[i]
    return "".join(n)


main()
def main():
    n=input("give a number to check: \n")
    if hill(n):
        print("Yes it is a hill number")
    else:
        print("No it is not a hill number")

def hill(n):
    i=0
    while i<len(n)-1 and n[i]<n[i+1]:
        i+=1
    if i==0 or i==len(n)-1:
        return False
    while i<len(n)-1 and n[i]>n[i+1]:
        i+=1

    return i==len(n)-1

main()
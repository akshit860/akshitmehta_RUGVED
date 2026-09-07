def triple_and(a,b,c):
    return a and b and c
def main():
    a=input("true or false \n").lower()=="true"
    b=input("true or false \n").lower()=="true"
    c=input("true or false \n").lower()=="true"
    result = triple_and(a, b, c)
    print(result)
main()
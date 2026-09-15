
string=input("Enter a string in small: ")
string=list(string)
n=(int)(input("Enter the value by which you want to cipher: "))
string1=""
for index in string:
    i=ord(index)
    if((ord(index)+n)>=97 and (ord(index)+n)<=122):
       string1+= chr(ord(index)+n)
    else:
        j=n-(122-i)
        string1+= chr(96+j)




print(string1)
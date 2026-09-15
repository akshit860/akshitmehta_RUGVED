string= input("Enter text: ")
words_100=[]
count=1
temp=""
for i in string:
    temp+=i
    if(i==' '):
        count+=1
    if(count%100==0):
        words_100.append(temp)
        temp=""
print(words_100)
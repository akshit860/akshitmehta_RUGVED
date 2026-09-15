import numpy as np
arr=input("Enter an array: ")
print(arr)
count=0
for i in range(0,len(arr)):
    for j in range(0, i):
        if(arr[i]==arr[j]):
            f=arr[i+1]
            g=i+2
            count=1
            break
        if(count==1):
            break
print("Element "+ f + " repeats at "+ (str)(g))
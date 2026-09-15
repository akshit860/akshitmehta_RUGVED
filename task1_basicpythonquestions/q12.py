n=(int)(input("Enter n: "))
for i in range(0, n):
    for j in range (0, n-i-1):
        print(' ',end='')
    for j in range(0, i+1 ):
        print('* ',end='')
    print()
for i in range(0,n):
   for j in range(0, i):
       print(' ', end='')
   for j in range(0, n-i):
       print('* ', end='')
   print()
N=int(input("Enter N: "))
count=(N-1)*2-1
n1=N*2-1
for i in range(0, N-1):
    for j in range(0, i+1):
        print( '*', end=" ")
    for j in range(0, count):
        print(' ', end=" ")
    for j in range(0, i+1):
        print('*', end=" ")
    print()
    count=count-2
for i in range(0,n1):
    print('* ',end='')
print()
for i in range(0, N-1):
    count = count + 2
    for j in range(0, N-i-1):
        print('*', end=" ")
    for j in range(0, count):
        print(' ', end=" ")
    for j in range(0, N-i-1):
        print('*', end=" ")
    print()
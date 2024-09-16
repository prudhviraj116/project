#all patterns in python
'''1
   22
   333
   4444
   55555
rows=5
for i in range(rows+1):
    for j in range(i):
        print(i,end='')
    print('')'''
'''1
   1 2
   1 2 3
   1 2 3 4
   1 2 3 4 5'''
'''rows=int(input('enter rows:'))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end='')
    print('')'''
'''1 1 1 1 1
   2 2 2 2
   3 3 3
   4 4
   5'''
'''rows=int(input('enter rows:'))
b=0
for i in range(rows,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end='')
    print('')'''
'''5 5 5 5 5
5 5 5 5
5 5 5
5 5
5'''
'''rows=int(input('enter rows:'))
num=rows
for i in range(rows,0,-1):
    for j in range(0,i):
        print(num,end='')
    print('')'''
'''1
   3 3 3
   5 5 5 5
   7 7 7 7 7
   9 9 9 9 9 9'''
rows=5
i=1
while i<=rows:
    j=1
    while j<=i:
        print(i*2-1,end='')
        j=j+1
    i=i+1
    print('')
        

   

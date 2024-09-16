#print 2 num product if the num<=1000 printb its sum
'''def multiply(num1,num2):
    product=num1*num2
    if product<=1000:
        return product
    else:
        return num1+num2
result=multiply(40,30)
print('the result is',result)'''
#print the sum of pervious current numbers
'''previous_num=0
for i in range(1,11):
    sum=previous_num+i
    print("current num",i,"previous_num",previous_num,"sum:" ,sum)
    previous_num=i'''
#string print even index values
'''s=input('enter a string:')
r=len(s)
for i in range(0,len(s)-1,2):
    print(i,s[i])'''
'''s=input('enter string:')
for i in s[4:]:
    print(i)'''
#soluthon2
'''def remove_char(s,n):
    x=s[n:]
    return x
print('removing first n characters from a string')
res=remove_char('prudhvi',4)
print (res)
res=remove_char('praneetha',2)
print(res)'''
#list first and last num same
'''list=[10,20,30,40,10]

if list[0]==list[4]:
        print(True)
else:
    print(False)'''
#solution2
'''def first_last_same(list):
    first_num=list[0]
    last_num=list[-1]
    if first_num==last_num:
        return True
    else:
        return False
list=[10,20,30,40,10]
print(first_last_same(list))
list=[75,35,46,30,60]
print(first_last_same(list))'''
#divisible by 5 in list
'''list=[10,20,33,46,55]
for i in list:
    if i%5==0:
        print(i)'''
#count of words in a string
'''s='emma is a developer. emma is a writter'
r=s.count('emma')
print(r)'''
#solution 2
'''def count(s):
    count=0
    for i in range(len(s)-1):
        count += s[i:i+4]=='emma'
    return count
count=count('emma is a developer.emma is a writter')
print('emma appered ',count,'times')'''
# print patterns
'''1
   2 2
   3 3 3
   4 4 4 4
   5 5 5 5 5
rows= int(input('enter rows:'))
for i in range(1,rows+1):
    for j in range(i):
        print(i,end='')
    print('')'''
#given number is pallandrom
'''def pallandrom(num):
    x=num
    reverse=0
    while num>0:
        y=num%10
        reverse=(reverse*10)+y
        num=num//10
    if x==reverse:
        print('pallandrom')
    else:
        print('not a pallandrom')
pallandrom(121)
pallandrom(125)'''
num=int(input('enter a number:'))
b=num
reverse=0
while num>0:
    x=num%10
    reverse=reverse*10+x
    num=num//10
if reverse==b:
    print('pallandrom')
else:
    print('not a pallandrom')
    

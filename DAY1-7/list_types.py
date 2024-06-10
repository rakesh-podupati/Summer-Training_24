'''l = [1,2,3,4,5]
for i in range(1,4):
    l[i - 2]= l[i]
for i in range(0,4):
    print(l[i],end=" ") 

l = [1,2,3]
l1=l
l[0] = 4
print(l1)
'''
'''list types
l=[22,33,]
append()
l.append([1,2,3])
print(l)
l=[99,98]
extend()
l.extend([1,2,3,4])
print(l)
l=99,98,1,2,3,4
  
   insert()
l.insert(idex number,adding element)
remove()
l=[1,2,3,4]
l.remove(2,3)
0/p=[1,4]
pop()

l=[1,2,3,4]
l.pop(-1)
o/p=[1,2,3]
index()
print(l.index(5))
count()'''



'''
a = list(map(int,input().split()))
b  =[]
a.sort()
for i in a:
    if i%2==0:
        b.insert(0,i)
    else:
        b.append(i)
print(b)'''





'''to know the sum of list values and max valuxe list index numbe
'''


n=int(input())
a = list(map(int,input().split()) for i in range(n))
m = 0
for i in a:
    s = sum(i)
    if s > m:
        m = s
        ind=a.index(i)
print(ind)
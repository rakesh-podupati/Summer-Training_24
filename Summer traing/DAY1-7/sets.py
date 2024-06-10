'''sets are unorderd 
example;
s=((1,2,3,4,5))
s=[{1,2,3,4}]
s={}
methods:

s.add()

s.update()

s.copy()

s.clear()

s.remove()

s.discard
print(s.pop())

union
print(a.union(b))

intersection
print(a.intersection(b))

a.inersection_update(b)
print(a)
difference()

'''

'''s={1,2,3,4,'hii','hello,''yyyy'}
print(s)
print(type(s))

s.add(9)
print(s)

r={9,8,7,6}
s.update(r)
print(s)

s1={1,2,3}
s1=s.copy()
print(s1)

a={1,2,3,4,5,6}
b={6,7,8,9}
c={11,33,6,7,8,1}
a.intersection_update(b,c)
print(a)


print(a.difference(b))
print(a-b)

r={99,98,97,96,1,2,3,4}
print("sorted",sorted(r))'''


a={1,2,3}
b={9,8,7,6,5}
print(1 in a)
print(2 not in a)
print(a==b)
print(a!=b)



res={s for s in [1,2,3] if s % 2==0}
print(res)

'''dictonary=unorderd,changable,and indexed 
index using key Value'''


'''methods
d.pop("a")
d.popitem()
d.clear()
print(d.(keys))

rint(d.(values))

print(d.(itrms()))'''


'''d = {1:'hi','a':123,100:32.4}

print(d[1])
print(d['a'])
print(d[100])
print(d.get('a'))
#modify and delete'''

'''r={1:'hel',2:100,5:1}
del(r)
print(r)'''





'''#fromkeys()#
d = {'a','b','c','d'}
d = dict.fromkeys(d,(10))
print(d)'''


'''d  ={1:'hi','a':123,100:32.4}
print(d.setdefault('a'))
print(d.setdefault('b'))
print(d)
print(d.setdefault('b',200))
print(d)'''




# NESTED DICTONARY'''
r ={1:'JI','A':123,100:{2:'C','X':1},'R':99}
print(r[100]['X'])



'''student = {"name":"emma",10:100}

print(del(r))'''



'''d={}
n=int(input("enter number of elements"))
for i in range(n):
    k=int(input("enter key"))
    v = int(input("value"))
    d[k]=v
key=int(input())
if key in d:
    del d[key]
print(d)'''



# keys= input().split()
# values = input().split()
# d = dict(zip(keys,values))
# print(d)


# l1=(input().split())
# l2=(input().split())
# d={}
# for i in range(0,3):
#     key=l1[i]
#     value=l2[i] 
#     d[key]=value
# print(d)



l={'a':100,'b':200,'c':300}
l1={'a':300,'b':200,'d':400}
combine_dist={}
for key in l:
    if key in l1:
        combine_dist[key]=l[key]+l1[key]
    else:
        combine_dist[key]=l[key]
for key in l1:
    if key not in combine_dist:
        combine_dist[key]=l1[key]
print("combine_distonary",combine_dist)


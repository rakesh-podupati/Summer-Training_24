''' used on lists
slice is a operation 
ex:
l= [1,2,3,4,5]
print([:])
[1,2,3,4,5]
print(l[2:])
[3,4,5]'''
'''l= [10,20,30,40,50]
print(l[:3])
print(l[3:])
print(l[0:4:2])
''''''1 starting point,4 end point,2 miss values ''''''
print(l[:4:])'''
'''n1=['python','flask','dijango','tikner']
n2=n1
n3=n1[:2]
n2[0]='scipy'
n3[1]='numpy'
s=10
for i in (n1,n1,n3):
    if i[0]=='python':
        s+=1
    if i[1]=='python':
        s+=2
print(s)
'''
'''
r=input()

print(len(r))'''
def l(str1):
    count=0
    for char in str1:
        count+=1
    return count 
str1=input()

print(l(str1))
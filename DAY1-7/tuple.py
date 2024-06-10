''' 
it is same like list but immutable
cannot modify'''
'''t=()'''
a=(1,2,3,4,5)
print(len(a))
print(max(a))
print(min(a))
print(all(a))
print(any(a))
print(a.index(5))
print((23 not in a))
print(a[:])
print(a[2:])
print(a[:5])
print(a[2:4])
print(a[-3:-1])
a=tuple(i*i for i in range(2,3))
print(a)

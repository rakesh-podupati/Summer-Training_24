a=list(map(int,input().split()))
a.sort()
b =[]
for i in a:
    if i not in b:
        b.append(i)
print(sum(b[-3:]))
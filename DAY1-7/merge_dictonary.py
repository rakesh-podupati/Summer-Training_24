d = {}
d1 = {}
n=int(input("no of elements"))
for i in range(n):
    k=input("enter key of first dict:")
    v=input("enter its value")
    d[k]=v
for i in range(n):
    k=input("enter key in dic:")
    v=input("enter value in dic:")
    d1[k]=v
d2=d.copy()
d2.update(d1)
print(d2)
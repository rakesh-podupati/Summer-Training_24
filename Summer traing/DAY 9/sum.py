T = int(input("enter t value"))
for x in range(T):
    A,B = map(int, input().split( ))
    print(A % B)
num=int(input())
rev = 0
while num>0:
    digit = num%10
    rev = rev*10+digit
print("REVERSE OF ",rev)
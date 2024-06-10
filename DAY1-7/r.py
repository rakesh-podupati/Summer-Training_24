# print('hello'.isupper())
# print('hello'.replace('l','r'))
# print('hello'.isalpha())
# print('hello'.isdecimal())
# print('hello'.islower())
# print('900'.isdigit())
# str = input()
# print(str[0])
# result =str[0]
# for i in range(1,len(str)):
#     if str[i]!=result[-1]:
#         result+=str[i]
# print(result)

'''str = input()
spaces=" "
result=" "

# for char in str:     #without spaces
    if char == " ":
        spaces +=char

    else:
        result +=char
final=spaces+result
print(final)'''




str1="hello"
str2="world"
# s3=" "
# for i in str1:
#     if str1 not in str2:
     
#      print(str1)
r_chars="".join(set(str1)^set(str2))
print(r_chars)


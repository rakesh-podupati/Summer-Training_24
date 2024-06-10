def authenticate():
    password="ranjith12"
    attempts=3
    while attempts>0:
        user_input=input("enter password")
        if user_input==password:
            print("welcome")
            break
        else:
            attempts-=1
            if attempts>0:
                print("wrong password",attempts)
            else:
                print("account blocked")
                break
authenticate() 

# l1=[1,2,8]
# l2=[3,4]
# print(id(l1[0]))
# print(id(l1[1]))
# print(id(l1[2 ]))
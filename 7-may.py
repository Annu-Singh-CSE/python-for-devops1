#conditional statement
#if else
#if elif else
#nested if else (chaining and ladder)

# name="annu"
# #if name=="annu":
# if name:
#     print(f"yes name {name} is provided")
#     address="noida"
#     if address:
#         print(f"yes address is : {address} provided")
#     else:
#         print(f"adress not provided")

# else:
#     print("name is not provided")


# num1=20
# if num1%2==0:
#     print("even")
#     mob=input("enter your number : ")
#     if len(mob) >= 10:
#         print("valid number")
#     else:
#         print("not valid numbrt")
# else:
#     print("odd")

#just like upsc exam work on multiple if else and work condition
student_name =input("enter your name :")
pre=int(input("enter your pre marks:"))
if pre >=400:
    print("your are pass in pre exam")

    mains=int(input("enter your mains marks :"))
    if mains >= 600:
        print("you are pass in mains exam and eligible for interview")
        inter=int(input("eneter your interview marks :  "))
        if inter >= 700:
            print(f"you are selected as IAS miss: {student_name}")
        else:
            print(f"you are fail in interview miss: {student_name}")
    else:
        print("fail in mains")

else:
    print("better luck next time , pre failed")

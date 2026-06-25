#error handling/file handlimg

try:
    n1=80
    n2=0
    res=n1/n2
    print=(res)
except Exception as e:
    print("Error : ",e)

finally:
    print("Thanks for visiting...")
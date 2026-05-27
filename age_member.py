min_age=18
nationality="indian"
user_age=int(input("enter you age:"))
user_id=input("enter your idently(ex.indian)")
if user_age >= min_age and user_id==nationality:
   print("user is eligible for voting")
else:
   print("user is not eligible for voting")


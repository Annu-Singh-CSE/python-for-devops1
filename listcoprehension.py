# emp_list=[]  #empty list hai yeh
# for i in range(1,11):
#     emp_list.append(i)  # all list print in one timeb append
#     print(emp_list)


#     # same code in one line how to wrote
# print([i**2 for i in range(1,11)]) # for square
# print([i for i in range(1,11) if i%2==0])#for even# for odd
# print([str(i)+":EVEN" if i%2==0 else str(i)+":ODD" for i in range(1,11)]) 

# emp_name=["annu", "anh" , "aggkkh"]
# res=[n.lower() for n in emp_name]
# #res=[n.upper() for n in emp_name]
# #res=["-".join(n) for n in emp_name]
# print(res)
   

# fruits_list=["apple","mango","papaya","banana","orange","grapes"]
# for i in fruits_list: 
#       if "n" in i:
#             print(i)

# fruits_list=["apple","mango","papaya","banana","orange","grapes"]
# user="p"
# res=[i.upper() for i in fruits_list if user in i]
# print(res)

#writ a function to check odd-enev number
def odd_even(n):
    if n%2==0:
     print("even")
    else:
      print("odd") 
odd_even(11)

def odd_even(n):
   if n%2==0:
      return "EVEN"
   else:
      return "ODD"   
res=odd_even(11)
print(res)


res=lambda x,y : x+y
print(res(134,20))

res=lambda x,y : x+y
print(res(10,20))
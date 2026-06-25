
#travelsing in loop
# name="python programming"
# size=len(name)
# for i in range(size):
#     print(name[0])

# # without range
# name="python"
# for i in name:
#     print(i)

# var1="Devops Engineer"
# for i in var1:
#     if i=="e" or i=="E":
#         continue
#     print(i,end=" ")

# wap to count all the voewal from given string : "this is devops batch"
# str1="this is devops batch"
# v_count=0
# c_count=0
# for i in str1:
#     if i in "aeiouAEIOU":
#         v_count+=1
#    # print(i , end= " ")
#     #print(v_count)
# else:
#     c_count=c_count+1

# print(v_count)
# print(c_count)

# #wap to  print  your in reverse formate
# name="annu"
# rev="" 
# for i in name:
#     rev=i+rev
# print(rev)

# print this type
#p PYTHON 0
#Y PYTHON 1
# T PYTHON 2
#H PYTHON 3
#O PYTHON 4
#N PYTHON 5

word = "PYTHON"
for index, char in enumerate(word):
    print(f"{char} {word} {index}")
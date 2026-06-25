# marks_10th=[20,90,78,90,"hello",5.5]
# print("before update : ",marks_10th)
# marks_10th[0]=200
# marks_10th[-1]=200
# i=8
# print(marks_10th[i]) # list index out of index
# print(len(marks_10th))
# print("after update : ", marks_10th)
# print("after update : ", marks_10th)

my_list = [10, 20, 30, 40]

first_elm = my_list[0]
last_elm = my_list[-1]

my_list[-1] = first_elm
my_list[0] = last_elm

print(my_list)

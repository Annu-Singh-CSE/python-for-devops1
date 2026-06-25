#for i in range(1,6):
 #   print(i,"first loop")
  #  for j in range(1,6):
   #     print(j,"inner loop")

#nested loop
#even onlu sum number use and add them
number=[1,11,111,22,23,33,44,45,556,667,88,99,88]
even_sum = 0
for i in number:
  if i % 2 == 0:
      even_sum += i
     print(f"even number:{i}")
print(f"sum of even number:{even_sum}")
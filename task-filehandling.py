para="""Annu is a DevOps engineer who studies for 3 hours every day. In 2026, he plans 
to complete 50 DevOps projects and earn 2 cloud certifications. He practices Python, Docker, Kubernetes, 
and AWS regularly. His goal is to improve his skills by 
100 and become a senior DevOps engineer within the next 5 years."""

count_digits = 0
total_char = 0
for i in para:
    if i in "0123456789":
        count_digits+=1
    else:
        total_char+=1

       # print(count_digit)
with open(f"stats.txt","w") as file:
    file.write(f"Total digit in file : {count_digits}")
    file.write("\n")
    file.write(f"Total chars in file : {total_char}")

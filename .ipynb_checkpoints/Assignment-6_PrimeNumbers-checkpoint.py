list_prime = []
a = 1
n = 100
for i in range(a, n + 1):
   if i > 1:
       for ii in range(2, i):
           if (i % ii) == 0:
            break
            print("Prime numbers between", a, "and", n, "are: ")
       else:
           #print(i)
           list_prime.append(i)
print(f"The prime number lists = {list_prime}")
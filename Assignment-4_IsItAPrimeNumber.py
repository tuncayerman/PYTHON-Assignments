number = int(input("Bir sayı giriniz: "))
result=True
for i in range(2, number):
    result = number%i and result
if result:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
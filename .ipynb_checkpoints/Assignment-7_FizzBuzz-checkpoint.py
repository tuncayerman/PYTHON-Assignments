numbers = list(range(1,100))
fizz_buzz = []

for i in numbers:
    if i % 3 == 0 and i % 5 != 0  :
        i = "Fizz"
        fizz_buzz.append(i)
    elif i % 5 == 0 and i % 3 != 0 :
        i = "Buzz"
        fizz_buzz.append(i)
    elif i % 3 == 0 and i % 5 == 0 :
        i = "FizzBuzz"
        fizz_buzz.append(i)
    else :
        fizz_buzz.append(i)
print(fizz_buzz)
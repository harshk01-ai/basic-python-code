#1. Print numbers from 1 to 100.


for i in range(1,101):
    print(i, end=" ")

#2. Print the multiplication table of a number.
n = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

#3. Print the sum of the first 10 natural numbers.
sum_ = 0
for i in range(1,11):
    sum_ += i
print(sum_)

#4. Print all even numbers from 1 to 50.
for i in range(1,51):
    if i % 2 == 0:
        print(i)

#5. Find the factorial of a number.
num = int(input("Enter a number: "))
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
print(factorial)

# 6. Print the first n Fibonacci numbers.
n = int(input("Enter a number: "))
a =0
b = 1
print("fibonacci numbers:")
for i in range(1,n+1):
    print(a)
    a, b = b, a+b

#7. Check whether a number is prime.
num = int(input("Enter a number: "))
count =0
for i in range(1,num+1):
    if num % i == 0:
        count +=1
if count == 2:
    print("number is prime:",num)
else:
    print("number is not prime:",num)

# 8. Count the number of digits in a number.
num = int(input("Enter a number: "))
count = 0
for i in range(1,num+1):
    if num == 0:
        break
    digit = num % 10
    count += 1
    num = num // 10
print(count)

#9Find the sum of digits of a number.
num = int(input("Enter a number: "))
dig_sum = 0

for i in range(1,num+1):
    if num == 0:
        break
    digit = num % 10
    dig_sum += digit
    num = num // 10
print(dig_sum)

# 10. Find the LCM of two numbers using a loop.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
if num1 > num2:
    strat = num1
else:
    strat = num2
for i in range(strat,num1*num2 +1):
    if i % num1 == 0 and i % num2 == 0:
        print("lcm is",i)
        break
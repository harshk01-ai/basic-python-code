# 1. Print numbers from 1 to 10 using a while loop.
i = 1
while i <= 10:
    print(i)
    i = i + 1

#2. Reverse a number.
num = int(input('Enter a number: '))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 +digit
    num = num // 10
print(rev)

#3. Check if a number is a palindrome.
num = int(input('Enter a number: '))
tem = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 +digit
    num = num // 10
if rev == tem:
    print('it is a palindrome number:',tem)
else :
    print('not a palindrome number:',tem)

#4. Keep taking input until the user enters 0.

while True:
    num = int(input('Enter a number: '))
    if num == 0:
        break

#5. Find the GCD (HCF) of two numbers using a while loop.
num1 = int(input('Enter a number1 : '))
num2 = int(input('Enter a number2 : '))

while num2 != 0:
    num1 , num2 = num2, num1%num2
    print("hcf :",num1)

#6. Print all odd numbers between two given numbers.
a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
if b > a:
    while a <= b:
        if a % 2 != 0:
            print("odd number:", a)
        a = a + 1
else:
    while b <= a:
        if b % 2 != 0:
            print("odd number:", b)
        b = b + 1

#7. Print the multiplication table using a while loop.
n = int(input('Enter a number: '))
print("multiplication number:" )
i = 1
while i <= 10:
    print(n,"x",i,"=",n*i)
    i = i + 1

#8. Print the sum of digits of a number using a while loop.
num = int(input('Enter a number: '))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print("sum :",sum)

#9. Generate Fibonacci series using a while loop.
n = int(input('Enter a number: '))
i = 1
a = 0
b = 1
while i <= n:

    print(a)
    a ,b = b,a+b
    i = i + 1


#10. Guessing game: keep asking the user to guess a number until correct.
secret = 7
while True:
    num = int(input('guess a number: '))
    if num == secret:
        print('the secret number is',secret)
        break
    else:
        print("enter guess  number is worng ,try again")



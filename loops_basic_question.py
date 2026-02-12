
n = int(input("Enter  number: "))
#1. Take a number n as input and print all numbers from 1 to n.
i = 1

while i <= n:
    print(i)
    i = i + 1

#2. Take a number n as input and print the sum of all numbers from 1 to n.
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1
print('sum of all number:',sum)

#3. Take a number n and print the sum of all even numbers from 1 to n.
i = 1
even_sum = 0
while i <= n:
    if i % 2 == 0:
        even_sum = even_sum + i
    i = i + 1
print('sum of all even numbers:',even_sum)

#4. Take a number n and print the sum of all odd numbers from 1 to n.
i = 1
odd_sum = 0
while i <= n:
    if i % 2 != 0:
        odd_sum = odd_sum + i
    i = i + 1
print('sum of all odd numbers:',odd_sum)

#5. Take a number n and print its multiplication table in proper format.
i = 1
print("multiplication table:")

while i <= 10:
    print(n ,'x',i,'=',n*i)
    i = i + 1

#Digit-based Logic

#1. Take an integer input and count the number of digits in it.
# Example: Input → 12345, Output → 5
Num = int(input("Enter a number: "))
count = 0
while Num > 0:
    digit = Num % 10
    count = count + 1
    Num = Num // 10
print('number of digit:',count)

#2. Take an integer input and find the sum of its digits.
# Example: Input → 1234, Output → 10
Num = int(input("Enter a number: "))
digit_sum = 0
while Num > 0:
    digit = Num % 10
    digit_sum += digit
    Num = Num // 10
print('sum of all digits:',digit_sum)

#3. Take an integer input and reverse the number.
# Example: Input → 9876, Output → 6789
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print('reverse the number:',rev)

#4. Take an integer input and check if it is a palindrome number
# Example: Input → 121, Output → Palindrome number
num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10
if rev == num:
    print('palindrome number:', num)
else:
    print('not palindrome number:', num)

#5. Take an integer input and find the product of its digits.
# Example: Input → 123, Output → 6
num = int(input("Enter a number: "))
product = 1
while num > 0:
    digit = num % 10
    product = product * digit
    num = num // 10
print('product of all digits:',product)


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

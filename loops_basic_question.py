#2. Take a number n as input and print the sum of all numbers from 1 to n.
n = int(input("Enter  number: "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1
print(sum)
#IF–ELSE QUESTIONS

#1. Write a program to check whether a number is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#2. Write a program to check if a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


#3. Write a program to check whether a person is eligible to vote (age ≥ 18).
age = int(input("Enter your age: "))
if age >= 18:
    print("You are young,eligible to vote.")
else:
    print("You are not young,not eligible to vote.")

#4. Write a program to find the largest of two numbers.
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
if x > y:
    print("The number is greater than the number.",x)
else:
    print("The number is greater than the number.",y)


#5. Write a program to check if a character is a vowel or consonant.
ch = input('enter character ')
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print(f"The character  {ch} is vowel ")
else:
    print(f"The character  {ch} is consonant ")


# 6. Write a program to check whether a number is divisible by 5 and 11.
x = int(input("Enter a number: "))
if x % 5 == 0 and x % 11 == 0:
    print("number is divisible by 5 and 11")
else:
    print("number is not divisible by 5 and 11")


#7. Write a program to check if a given year is a leap year.
year = int(input("Enter a year: "))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#NESTED IF–ELSE QUESTIONS

#1. Write a program to check whether a number is positive, negative, zero, and if positive, check if it
# is even or odd.
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#2. Write a program to input marks and print the grade (A/B/C/D/Fail).
marks = int(input("Enter a number: "))

if marks > 90:
     grade = 'A'
     print("The grade is .",grade)
elif marks > 75:
    grade = 'B'
    print("The grade is ",grade)
elif marks > 60:
    grade = 'C'
    print("The grade is ",grade)
elif marks > 40:
    grade = 'D'
    print("The grade is ",grade)
else:
    grade = 'Fail'
    print("The grade is ",grade)

#3. Write a program to check if a person is Child/Teenager/Adult/Senior.
age = int(input("Enter your age: "))
if age <= 12:
    print("child")
elif age <= 18:
    print("teenager")
elif age <= 59:
    print("adult")
else:
    print("senior")

#4. Write a program to input three numbers and print the largest.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a > b and a > c:
    print(f"largest is {a}")
elif b > a and b > c:
    print(f"largest is {b}")
else:
    print(f"largest is {c}")


#5. Write a program to find the type of triangle based on the sides.
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")

else:
    print("Not a valid triangle")

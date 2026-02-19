#Basic List Questions

# 1. Create a list of 5 arbitrary numerical values and print the list to the console.
li = [1,2,3,4,5]
print(li)

# 2. Given a list, write code to display only the first and the last element.

li = [1,2,3,4,5]
last_index = len(li)-1
print("first element",li[0],"last element",li[last_index] )

# 3. Determine and print the total number of elements in a list without utilizing the
# built-in len() function.

lst = [1,6,3,4,5]
count = 0
for i in lst:
    count += 1
    print(i)
print("total number in list",count)

# 4. Modify a given list by adding a new element to its end, solely using list indexing
# and assignment (without using the append() method).

lst = [1,6,3,4,5]
lst[len(lst)-1] = 2
print(lst)

# 5. In a pre-defined list, change the value of the element located at the third index
# position with a new specified value.

lst = [1,6,3,4,5]
lst[3] = 45
print(lst)

# 6. Develop a script that accepts 5 distinct inputs from the user and stores all of them
# sequentially in a single list.

li =[]

for i in range(1,6):
    Input = input("input data")
    li.append(Input)

print(li)

# 7. Iterate through a given list using a for loop and print each element on a new line.

lst = [1,6,3,4,5]
for i in lst:
    print(i)


# 8. From a given list of integers, write code to print only the numbers that are even.

lst = [1,6,3,4,5]
print("even number in list:")
for i in lst:
    if i%2==0:
        print(i)


# 9. For a given list and a target number, calculate and print the total number of
# occurrences of the target number within the list.

lst = [1,6,3,4,5,1,6,5,5]
target = 5
count = 0
for i in lst:
    if i == target:
        count += 1
print(count)


# 10. Calculate and print the sum of all numerical elements in a list without using the
# built-in sum() function.
lst = [1,6,3,4,5]
sum = 0
for i in lst:
    sum += i
print(sum)


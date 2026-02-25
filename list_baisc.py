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
el_sum = 0
for i in lst:
    el_sum += i
print(el_sum)

# Intermediate List Questions

# 1. Identify and print the largest element present in a list of numbers without using the
# built-in max() function.

lst = [1,6,3,4,5]
largest = 0
for i in lst:
    if i > largest:
        largest = i
print(largest)


# 2. Identify and print the smallest element present in a list of numbers without using
# the built-in min() function.
lst = [1,6,3,4,5]
smallest = lst[0]

for i in lst:
    if i < smallest:
        smallest = i
print(smallest)


# 3. Create a new list that contains the elements of the original list in reverse order,
# without using the reverse() method or list slicing.

lst = [1,6,3,4,5]
new_list = []
for i in range(len(lst)-1):
    new_list.append(lst[i])
print(new_list)

# 4. Sort a list of numbers in ascending order using the logic of the Bubble Sort
# algorithm, without using the built-in sort() method.

lst = [1,6,3,4,5]
for i in range(len(lst)-1):
    for j in range(len(lst)-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)


# 5. Generate a new list from an original list, where all duplicate elements have been
# removed, without using the built-in set() function.

org_list = [1,6,3,4,5]
new_list = []
for i in org_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)


# 6. Write a boolean function that checks whether a specified element is contained
# within a given list.
lst = [1,6,3,4,5]
el = int(input("enter element:"))
el_has = False
for i in lst:
    if el == i:
        el_has = True
        break
print(el_has)

# 7. Print only the elements from a list that are located at an index position which is an
# even number (0, 2, 4, ...).

lst = [1,6,3,4,5]
for i in range(0,len(lst),2):
    print(lst[i])


# 8. Print only the elements from a list that are located at an index position which is an
# odd number (1, 3, 5, ...).
lst = [1,6,3,4,5]
for i in range(1,len(lst),2):
    print(lst[i])


# 9. Iterate through a list of integers and separately count and print the total number of
# even numbers and the total number of odd numbers.
lst = [1,6,3,4,5]
even_count = 0
odd_count = 0
for i in lst:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even count:",even_count)
print("odd count:",odd_count)

# 10. Given a list of numbers, create and print a second list where each element is the
# square of the corresponding element in the original list.

org_list = [1,6,3,4,5]
new_list = [x*x for x in org_list]
print(new_list)

# 11. Combine the elements of two separate lists into a single new list without using the
# + or extend() operators.

a = [1,2,3,4,5]
b = [6,7,8,9]
new_list = []
for i in a:
    new_list.append(i)
for i in b:
    new_list.append(i)
print(new_list)

# 12. Modify a list in place so that all numbers less than zero (negative numbers) are
# removed.
lst = [0,0,1,2,0,5,3,-1,-2]
lst2 = lst.copy()
for i in lst2:
    if i < 0:
        lst.remove(i)
print(lst)

# 13. Determine and print the second largest numerical value in a list without applying
# any sorting techniques.

lst = [1,6,3,4,5]
largest = 0
sec_largest = 0
for i in lst:
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest and i != largest:
        sec_largest = i
print(largest)
print(sec_largest)


# 14. Implement a cyclic shift operation on a list where every element is moved one
# position to the right, and the last element wraps around to the first position.

lst = [1,6,3,4,5]
time = int(input("enter time:"))
for i in range(time):
    lst.insert(0,lst.pop())
print(lst)

# 15. Write a function that returns True if a list is currently arranged in ascending order,
# and False otherwise.
lst = [1,3,4,5]

def check_asce(lst):
    for i in range(len(lst)):
        if lst[i] > lst[i+1]:
            return False
    return True
print(check_asce(lst))

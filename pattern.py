"""
1. Square of stars
*****
*****
*****
*****
*****
"""
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("*", end=" ")
    print()


"""
2. Right-angled triangle
*
**
***
****
*****
"""
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

"""
3. Inverted right-angled triangle
*****
****
***
**
*
"""
n = 5
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()

"""
4. Triangle with numbers
1
12
123
1234
12345
"""
n = 5
for i in range(1, n + 1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

"""
5. Same number triangle
1
22
333
4444
55555
"""

n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

"""
6. Square of numbers
11111
22222
33333
44444
55555
"""

n = 5
for i in range(1, n + 1):
    for j in range(1, n+1):
        print(i, end=" ")
    print()

"""
7. Triangle of alphabets
A
AB
ABC
ABCD
ABCDE
"""
n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(65+j), end=" ")
    print()

"""
8. Square of alphabets
AAAAA
BBBBB
CCCCC
DDDDD
EEEEE
"""
n = 5
for i in range(n):
    for j in range(n):
        print(chr(65+i), end=" ")
    print()

"""
9. Decreasing number pattern
12345
1234
123
12
1
"""
n = 5
for i in range(n):
    for j in range(1,n+1-i):
        print(j, end=" ")
    print()

"""
10. Continuous number triangle
1
2 3
4 5 6
7 8 9 10
"""
n = 5
num = 1
for i in range(1,n):
    for j in range(i):
        print(num, end=" ")
        num = num + 1
    print()

"""
11. Pyramid of stars
    *
   ***
  *****
 *******
*********
"""
n = 5
for i in range(1,n+1):
    for k in range(n-i):
        print(" ", end=" ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()

"""
12. Inverted pyramid
*********
 *******
  *****
   ***
    *
"""
n = 5
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(2*(n-i)- 1):
        print("*", end=" ")
    print()

"""
13. Diamond pattern
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()
for i in range(n-1,-1,-1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()

"""
14. Number pyramid
    1
   121
  12321
 1234321
123454321
"""
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(1,i+1):
        print(k, end=" ")
    for k in range(i-1,0,-1):
        print(k, end=" ")
    print()

"""
15. Hollow square
*****
*   *
*   *
*   *
*****
"""
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == n or i == 1 or j == n or j == 1 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
16. Hollow right triangle
*
**
* *
*  *
*****
"""
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == n or j == 1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
17. Hollow pyramid
    *
   * *
  *   *
 *     *
*********
"""
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(1,2*i):
        if k == 1 or  i == n or k ==2*i -1 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
A
B C
D E F
G H I J
"""
n = 5
num = 65
for i in range(1,n):
    for j in range(i):
        print(chr(num), end=" ")
        num = num + 1
    print()

"""

19. Mirrored right triangle
    *
   **
  ***
 ****
*****

"""
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(n,n-i,-1):
        print("*", end=" ")
    print()

"""
20. Sandglass pattern
*****
 ****
  ***
   **
    *
   **
  ***
 ****
*****
"""
n = 5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(0,i):
        print("*", end=" ")
    print()
for i in range(2,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()


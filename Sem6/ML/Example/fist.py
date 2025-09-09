"""Converted from fist.ipynb"""

a=2
b=10

print(a+b)

a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print(a+b)

sum = 0
for i in range(10):
    sum += int(input("Enter a number: "))
print(sum)

def sum(a, b):
    return a + b


print(sum(2, 3))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

dir = {"Germany": "Berlin", "Canada": "Ottawa", "England": "London"}
print(dir["Canada"])


dir["Italy"] = "Rome"
print(dir)

del dir["Germany"]
print(dir)

list = [1, 2, -8, 10, 12, 13]
product = 1
for i in list:
    product *= i
print(product)

print(list[0:2])

print(list[-3:])

print(list[2:4])


def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


print(largest(2, 3, 4))
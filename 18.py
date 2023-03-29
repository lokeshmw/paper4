# Index error#####
import math


def func1(a):
    try:
        raise print(a[5])

    except IndexError:
        print(f"list contains {len(a)} elements and given index is out of range")


A = [1, 2, 3]
func1(A)


# Type error#####

def func2(a, b):
    try:
        raise print(a + b)

    except TypeError:
        print(f"{a} and {b}  are diff data types, they cant be concatenated")


x = "loki"
y = 4
func2(x, y)


# Attribute error#####

def func3(a, b):
    try:
        raise a.apppend(b)

    except AttributeError:
        print(f"{a} has no attribute ie append(), so {b} cant be appended ")


x = "loki"
y = 4
func3(x, y)


# Value error#####

def func4(a):
    try:
        raise print(math.sqrt(a))
    except ValueError:
        print(f"{a} is invalid ")


y = -4
func4(y)

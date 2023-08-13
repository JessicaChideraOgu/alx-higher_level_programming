#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    """This prints the sum(+), difference(-),
    multiplication(*) and division(/) of 10 and 5."""

a = 10
b = 5

total_1 = add(a, b)
total_2 = sub(a, b)
total_3 = mul(a, b)
total_4 = div(a, b)

print("{} + {} = {}".format(a, b, total_1))
print("{} - {} = {}".format(a, b, total_2))
print("{} * {} = {}".format(a, b, total_3))
print("{} / {} = {}".format(a, b, total_4))

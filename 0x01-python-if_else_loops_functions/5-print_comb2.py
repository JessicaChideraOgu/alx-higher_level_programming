#!/usr/bin/python3
for a in range(100):
    if a < 99:
        print(f"{a:02d}".format(a), end=", ")
    else:
        print("\n")

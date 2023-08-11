#!/usr/bin/python3
for a in range(100):
    if a < 100:
        print(f"{a:02d}".format(a), end=", ")
    else:
        print("\n")

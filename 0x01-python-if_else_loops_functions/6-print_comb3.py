#!/usr/bin/python3
for p in range(0, 9):
    for k in range(p + 1, 10):
        if p == 8:
            print("{}{}".format(p, k))
        else:
            print("{}{}".format(p, k), end=", ")

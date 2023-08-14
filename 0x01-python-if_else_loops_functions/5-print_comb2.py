#!/usr/bin/python3
for i in range(100):
    print("{:02d}, ".format(i), end="")
    if i == 98:
        print("{:2d}".format(i + 1))
        break

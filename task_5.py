#!/usr/bin/env python3

a = [int(number) for number in input().split()]
for number in range(1, len(a)):
    if (a[number] > 0 and a[number - 1] > 0) or (a[number] < 0 and a[number - 1] < 0):
        print(a[number - 1], a[number])
        break

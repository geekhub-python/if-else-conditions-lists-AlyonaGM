#!/usr/bin/env python3

m = int(input())
n = int(input())
k = int(input())
if ((k % m == 0) or (k % n == 0)) and k < m * n:
    print("YES")
else:
    print("NO")
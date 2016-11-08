#!/usr/bin/env python3

my_list= input().split()
pairs = sum(my_list[i + 1:].count(my_list[i]) for i in range(len(my_list)))
print(pairs)


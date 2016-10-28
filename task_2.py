#!/usr/bin/env python3

print("Ввод")
first = int(input())
second = int(input())
third = int(input())
if first == second == third:
	print("Вывод", "3")
elif first == second or first == third or second == third:
	print("Вывод", "2")
else:
	print("Вывод", "0")
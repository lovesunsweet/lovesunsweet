#!/usr/bin/env python3

import sys

def calculator(salary):
	tax = salary - 3500
	if salary <= 0:
		return '0.00'
	elif tax <= 1500:
		x = 0.03
		a = 0
	elif tax <= 4500: 
		x = 0.1
		a = 105
	elif tax <= 9000:
		x = 0.2
		a = 555
	elif tax <= 35000:
		x = 0.25
		a = 1005
	elif tax <= 00:
		x = 0.3
		a = 2755
	elif tax <= 80000:
		x = 0.35
		a = 5505
	else:
		x = 0.45
		a = 13505
	payable =  tax * x - a
	return format(payable, ".2f")

if __name__ == '__main__':
	if len(sys.argv) == 2:
		try:
			salary = int(sys.argv[1])
		except ValueError:
			print("Parameter Error")
		print(calculator(salary))
	else:
		print("Parameter Error")


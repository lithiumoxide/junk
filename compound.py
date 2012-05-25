#! /usr/local/bin/python

import math

init = input('Initial investment: ')
month = input('Monthly addition: ')
int = input('Interest rate (%): ')
yrs = input('Number of years: ')

intr = int*0.01

for i in range(0,yrs):
	yearly = init+(12*month)
	compound = yearly+(intr*yearly)
	init = compound

print compound

#! /usr/local/bin/python

def fact(n,f):
	f=1
	while n>1:
		f = f*n*(n-1)
		n = n-2
	return f

n = input('Number: ')
print fact(n,f=1)
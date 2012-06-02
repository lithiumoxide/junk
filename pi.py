#! /usr/local/bin/python

# An attempt to build a pi calculator based on the Chudnovsky & Chudnovsky method
# A work in progress

import sys
import math
import string

alg = 0

for k in range(1,5):
	fact1 = reduce(lambda i,j : i*j, range(1, ((-1**k)*6*k)+1))
	fact2 = reduce(lambda x,y : x*y, range(1, (3*k)+1))
	fact3 = reduce(lambda a,b : a*b, range(1, k+1))

	alg = alg + (fact1*(13591409+(545140134*k))) / (fact2*(fact3**3)*640320**((3*k)+(3/2)))

print alg
print alg*12
print 1/(alg*12)
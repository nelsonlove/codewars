"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_of_multiples(factors, limit):
	multiples = []
	for i in range(min(*factors), limit):
		for factor in factors:
			if i % factor == 0:
				multiples.append(i)
				break
	return sum(multiples)


print(sum_of_multiples([3, 5], 1000))

"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def prime_factors(n):
    divisor = 2
    factors = []
    while n + 1 > divisor:
        if n % divisor == 0:
            factors.append(divisor)
            n = n / divisor
            divisor = 2
        else:
            divisor += 1
    return factors


print(prime_factors(600851475143)[-1])

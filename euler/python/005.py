"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""


def primes(limit):
    n = 3
    primes_list = [2]
    while n < limit:
        divisor = 2
        is_prime = False
        while not is_prime:
            if divisor > n / 2:
                is_prime = True
            elif n % divisor == 0:
                is_prime = False
                break
            else:
                divisor += 1
        if is_prime:
            primes_list.append(n)
        n += 1
    return primes_list


def prime_factors(n):
    factors = []
    candidate_primes = primes((n + 2) / 2)
    while candidate_primes:
        divisor = candidate_primes[0]
        if n % divisor == 0:
            n = n / divisor
            factors.append(divisor)
        else:
            candidate_primes.pop(0)
    if not factors:
        factors.append(n)
    return factors


def smallest_evenly_divisible(limit):
    x = 2
    factors = []
    for x in range(2, limit + 1):
        x_factors = prime_factors(x)
        for f in factors:
            if f in x_factors:
                x_factors.remove(f)
        factors += x_factors
    out = 1
    for n in factors:
        out *= n
    return out


print(smallest_evenly_divisible(20))

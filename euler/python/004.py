"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome(n):
    def is_palindrome(n_):
        return str(n_) == str(n_)[::-1]

    largest = 0
    for i in reversed(range(1, n + 1)):
        for j in reversed(range(1, n + 1)):
            if is_palindrome(i * j) and i * j > largest:
                largest = i * j
    return largest


print(largest_palindrome(999))

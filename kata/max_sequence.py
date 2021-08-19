"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of
integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If
the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""


def max_sequence(arr):
    max_sum = 0

    if all([n < 0 for n in arr]):
        return max_sum

    for i, _ in enumerate(arr):
        sub_arr = arr[i:]
        while sub_arr:
            if sum(sub_arr) > max_sum:
                max_sum = sum(sub_arr)
            sub_arr.pop(-1)

    return max_sum

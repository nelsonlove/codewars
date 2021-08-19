"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the
alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""

import string


def rot13_cipher_encode(message):
    char_lists = [string.ascii_lowercase, string.ascii_uppercase]
    result = []
    for char in message:
        if all([char not in char_list for char_list in char_lists]):
            result.append(char)
            continue

        for char_list in [string.ascii_lowercase, string.ascii_uppercase]:
            if char in char_list:
                i = char_list.index(char) + 13
                if i > 25:
                    i -= 26
                result.append(char_list[i])
    return ''.join(result)

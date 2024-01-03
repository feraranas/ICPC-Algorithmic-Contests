
import math


def rotationalCipher(input_str, rotation_factor):
    if rotation_factor < 0:
        return input_str

    for i in range(len(input_str)): # O(n)
        if input_str[i].isnumeric():
            result += chr((int(ord(input_str[i]) - ord('0') + rotation_factor) % 10) + ord('0'))
        elif input_str[i].isalpha():
            if input_str[i].islower():
                result += chr((ord(input_str[i]) - ord('a') + rotation_factor) % 26 + ord('a'))
            elif input_str[i].isupper():
                result += chr((ord(input_str[i]) - ord('A') + rotation_factor) % 26 + ord('A'))
        else:
            result += input_str[i]

    return result

#!/usr/bin/python3
def roman_to_int(roman_string: str) -> int:
    if (roman_string is None) or (type(roman_string) is not str):
        return 0
    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10,
                  'V': 5, 'I': 1}
    sum = 0
    for i in range(len(roman_string)):
        if (i < len(roman_string) - 1):
            if roman_dict[roman_string[i]] >= roman_dict[roman_string[i + 1]]:
                sum += roman_dict[roman_string[i]]
            else:
                sum += 0 - roman_dict[roman_string[i]]
        else:
            sum += roman_dict[roman_string[i]]
    return sum

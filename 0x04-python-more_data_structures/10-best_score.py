#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(list(a_dictionary)) == 0:
        return None
    maxi = max([a_dictionary[keys] for keys in a_dictionary])
    for key in a_dictionary:
        if a_dictionary[key] == maxi:
            return key

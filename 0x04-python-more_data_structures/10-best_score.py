#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        n = max(a_dictionary, key=a_dictionary.get)
        return n
    else:
        return 'None'

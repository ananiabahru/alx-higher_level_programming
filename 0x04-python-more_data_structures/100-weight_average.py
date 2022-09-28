#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        number = 0
        denom = 0

    for tup in my_list:
        number += (tup[0] * tup[1])
        denom += (tup[1])

        return (number / denom)
    return 0


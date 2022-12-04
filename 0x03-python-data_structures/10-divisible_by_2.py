#!/usr/bin/python3
# divisible_by_2
# finds all multiples of 2 in a list


def divisible_by_2(my_list=[]):

    if len(my_list) == 0:
        return (None)

    div_2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            div_2.append(True)
        else:
            div_2.append(False)
    return (div_2)

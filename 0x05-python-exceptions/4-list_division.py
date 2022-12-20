#!/usr/bin/python3
# list_division:  divides element by element 2 lists.

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    while i < list_length:
        result = 0
        try:
            result = my_list_1 [i] / my_list_2[i]
        except TypeError:
                        print("wrong type")
        except ZeroDivisionError:
                        print("division by 0")
        except IndexError:
                        print("out of range")
        finally:
                        new_list.append(result)
    return (new_list)

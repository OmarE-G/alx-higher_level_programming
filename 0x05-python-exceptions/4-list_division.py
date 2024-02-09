#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_length = []
    for i in range (max(len(my_list_1), len(my_list_2))):
        x = 0
        try:
            x = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
            continue
        finally:
            try:
                list_length.append(x)
            except TypeError:
                continue
    return list_length

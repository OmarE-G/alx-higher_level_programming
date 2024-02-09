#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    for i in range (max(len(my_list_1), len(my_list_2))):
        try:
            x = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            print("divison by zero")
            x = 0
        except TypeError:
            print("wrong type")
            x = 0
        except IndexError:
            print("out of range")
        finally:
            list_length[i] = x
    return list_length          
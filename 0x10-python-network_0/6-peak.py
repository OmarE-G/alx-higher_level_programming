'''module to find peak'''


def find_peak(list_of_integers):
    '''find peak in a list of integers'''
    peak = 'None'
    for i in range(1, len(list_of_integers) - 1):
        if (list_of_integers[i] >
                max(list_of_integers[i-1], list_of_integers[i+1])):
            peak = list_of_integers[i]
            break
    return peak

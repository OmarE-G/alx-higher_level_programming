#!/usr/bin/python3
'''module to find peak'''


def find_peak(arr):
    '''find peak in a list of integers'''
    peak = None
    ln = len(arr)
    if ln > 1 and arr[0] > 1:
        return arr[0]
    if ln > 1 and arr[ln-1] > arr[ln-2]:
        return arr[ln-1]

    for i in range(1, ln - 1):
        if (arr[i] >
                max(arr[i-1], arr[i+1])):
            peak = arr[i]
            break
    return peak

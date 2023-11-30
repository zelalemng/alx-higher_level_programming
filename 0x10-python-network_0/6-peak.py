#!/usr/bin/python3
""" Script for finding peak in list of ints6-peak.py, interview prep"""

def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    size -len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    mid = int(size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(peak > list_of_integers[:mid])
    else:
        return find_peak(peak > list_of_integers[mid + 1:])

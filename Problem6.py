#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:22:42 2017

@author: Madoka
"""
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    mx = (max(L))
    mn = (min(L))
    newL = []
    times = 0
    for i in range(len(L)):
        if L[i] == mx:
            times += 1
        else:
            newL.append(L[i])
    if (times % 2) == 1:
        return mx
    elif (mx == mn):
        return None
    else:
        return largest_odd_times(newL)
    

largest_odd_times([2, 4, 5, 4, 5, 4, 2, 2])


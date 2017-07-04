#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 11:25:28 2017

@author: Madoka
"""

s = "This is great!"

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    newS = []
    s = list(s)
    for char in s:
        if not (char == 'a' or char == 'e' or char == 'i' or \
           char == 'o' or char == 'u' or \
           char == 'A' or char == 'E' or char == 'I' or \
           char == 'O' or char == 'U'):
            newS.append(char)
    s = ''
    s = ''.join(newS)
    print (s)
    
print_without_vowels(s)
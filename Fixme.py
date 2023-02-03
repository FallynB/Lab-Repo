#!/usr/bin/python3

def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    return [i for i in range(n + 1) if i % 2 == 0]

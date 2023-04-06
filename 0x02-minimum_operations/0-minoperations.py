#!/usr/bin/python3
"""
Minimum Operations module"""

def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while factor <= n:
        if n % factor == 0:
            operations += factor
            n /= factor
        else:
            factor += 1
    
    return operations

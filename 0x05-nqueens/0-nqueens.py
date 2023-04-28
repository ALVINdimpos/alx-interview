#!/usr/bin/python3
"""Solving the N Queens problem"""
import sys


args = sys.argv

if len(args) != 2:
    print("Usage: nqueens N")
    exit(1)

if args[1].isdigit() is False:
    print("N must be a number")
    exit(1)

layout = int(args[1])
if layout < 4:
    print("N must be at least 4")
    exit(1)


def check_here(nlist, index, curr_num):
    for item in nlist:
        if index == item[1] or\
                index == item[1] - (curr_num - item[0]) or\
                index == item[1] + (curr_num - item[0]):
            return 1
    return list([curr_num, index])


def loop_n_find(nlist, curr_num):
    if (curr_num > layout):
        return

    if len(nlist) == layout:
        print(nlist)
        return

    j = 0
    while j < layout:
        val = check_here(nlist, j, curr_num)
        if type(val) is list:
            new_nlist = nlist.copy()
            new_nlist.append(val)
            loop_n_find(new_nlist, curr_num + 1)
        j += 1
    return


for i in range(layout):
    arr = [[0, i]]
    loop_n_find(arr, 1)

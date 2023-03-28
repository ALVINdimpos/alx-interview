#!/usr/bin/python3
"""
Module for canUnlockAll function"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """
    if boxes is None or len(boxes) == 0:
        return False
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    return len(keys) == len(boxes)

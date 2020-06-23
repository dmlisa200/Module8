"""
program:  set_membership.py
author:  Lisa Kilmer
last modified:  6-22-2020
This program declares a set and the in_set function takes a letter as an argument
and if the letter is in the list return True and if not in list return False
"""
a = set('abcdefg')


def in_set(letter):
    if letter in a:
        return True
    else:
        return False


if __name__ == '__main__':
    in_set('d')


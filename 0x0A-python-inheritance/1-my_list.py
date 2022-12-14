#!/usr/bin/python3

'''A module for a Class which inherits from ``list`` class'''


class MyList(list):
    '''A subclass of ``list`` with extra public methods'''

    def print_sorted(self):
        '''prints out a list in a sorted order'''
        print(sorted(self))

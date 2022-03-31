#! ./pytest_project/pytest-env/bin/python3.8
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:51:23 2021

@author: Feliú Sagols
"""


def csv_reader(file_name):
    """
    Reader generator
    :param file_name: str
        File to read
    :return:
        str
        Next text line in file_name.
    """
    for row in open(file_name):
        yield row
        print("Reentrant point")


line_count = 0
for line in csv_reader('yield_example.py'):
    line_count += 1

print(f"Number of lines {line_count}")

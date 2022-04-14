"""the lib"""
import re

def join(list, seperator=''):
    stringVal = ''
    count = 0
    for item in list:
        if count < len(list):
            stringVal += item + seperator
        else:
            stringVal += item

    return stringVal

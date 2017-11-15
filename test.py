# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import svntools.remote as re
import svntools.local as lc
import base64
from Crypto import Random
import collections


def binary_search(str_search, deque):
    low = 0
    high = len(deque)-1
    while low <= high:
        mid = int((low+high)/2)
        if deque[mid] == str_search:
            print("已找到:%s" % str_search)
            return mid
        elif deque[mid] > str_search:
            high = mid-1
        elif deque[mid] < str_search:
            low = mid+1
    print("未找到:%s" % str_search)
    return -1

if __name__ == '__main__':
    deque_str1 = collections.deque()
    deque_str2 = collections.deque()
    for temp_str in range(0, 100000):
        deque_str1.append(temp_str)
    for temp_str in range(0, 100000, 2):
        deque_str2.append(temp_str)
    print(deque_str1)
    print(deque_str2)
    for deque_str1_temp in deque_str1:
        binary_search(deque_str1_temp, deque_str2)


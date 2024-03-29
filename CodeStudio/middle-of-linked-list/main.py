from math import *
from collections import *
from sys import *
from os import *

'''

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''


def findMiddle(head):
    slow = fast = head
    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    return slow

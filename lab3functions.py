from typing import *
from dataclasses import dataclass
import unittest
import math
import sys
sys.setrecursionlimit(10**6)

from plots import has_dup, Node


class Tests(unittest.TestCase):
    def test_has_dup(self):
        self.assertFalse(has_dup(None))
        self.assertFalse(has_dup(Node(1, None)))
        # Two nodes with same value has duplicate
        self.assertTrue(has_dup(Node(1, Node(1, None))))
        # Two nodes with different values has no duplicate
        self.assertFalse(has_dup(Node(1, Node(2, None))))
        # Duplicate appears later in list
        self.assertTrue(has_dup(Node(1, Node(2, Node(1, None)))))
        # Longer list with no duplicates
        self.assertFalse(has_dup(Node(1, Node(2, Node(3, None)))))
        # Adjacent duplicate (e.g. at end)
        self.assertTrue(has_dup(Node(1, Node(2, Node(2, None)))))
        # All nodes have the same value
        self.assertTrue(has_dup(Node(5, Node(5, Node(5, None)))))

# Remember from Lab 1: this if statements checks
# whether this module (ghg.py) is the module
# being executed or whether it's just being
# imported from some other module.
if (__name__ == '__main__'):
    unittest.main()
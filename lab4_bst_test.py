import sys
import unittest
from typing import *
from dataclasses import dataclass
import math
sys.setrecursionlimit(10**6)

from bst import *

def comes_before_int(int1: int, int2: int) -> bool:
    return int1<int2


def comes_before_str(str1: str, str2: str) -> bool:
    return str1<str2

@dataclass(frozen = True)
class Point2:
    x: int
    y: int

def comes_before_point2(point1: Point2, point2: Point2) -> bool:
    return math.sqrt(point1.x**2+point1.y**2) < math.sqrt(point2.x**2+point2.y**2)

bst_int = BinarySearchTree(comes_before_int, BTNode(10, BTNode(6, BTNode(5, None, None), None), BTNode(12, BTNode(11, None, None), None)))
bst_str = BinarySearchTree(comes_before_str, BTNode("f", BTNode("d", BTNode("b", None, None), None), BTNode("n", BTNode("m", None, None), None)))
bst_point2 = BinarySearchTree(comes_before_point2, BTNode(Point2(4, 6), BTNode(Point2(5, -3), BTNode(Point2(-1, -1), None, None), None), BTNode(Point2(7, -9), BTNode(Point2(8, -8), None, None), None)))


class BSTTests(unittest.TestCase):
    def test_comes_before_int(self):
        self.assertTrue(bst_int.func(2, 5))
    def test_comes_before_str(self):
        self.assertTrue(bst_str.func("abcde", "bcdef"))
    def test_comes_before_point2(self):
        self.assertTrue(bst_point2.func(Point2(2, -4), Point2(-6, 5)))

if (__name__ == '__main__'):
    unittest.main()
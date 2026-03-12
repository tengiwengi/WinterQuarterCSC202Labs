from typing import *
import unittest
import math
import matplotlib.pyplot as plt
import numpy as np
import sys
from dataclasses import dataclass
import functions
sys.setrecursionlimit(10**9)



# This is for reference; you can get rid of this function if you want.
def example_graph_creation() -> None:
    # Return log-base-2 of 'x' + 5.
    def f_to_graph( x : float ) -> float:
        return math.log2( x ) + 5.0
        
    # here we're using "list comprehensions": more of Python's
    # syntax sugar.
    x_coords : List[float] = [ float(i) for i in range( 1, 100 ) ]
    y_coords : List[float] = [ f_to_graph( x ) for x in x_coords ]
    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array
    # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )
    plt.plot( x_numpy, y_numpy, label = 'log_2(x)' )
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Example Graph")

IntList : TypeAlias = Union[None,'Node']

@dataclass(frozen=True)
class Node:
    val: int
    next: Union[None, "Node"]

def range(max_exclusive: int) -> IntList:
    if max_exclusive <= 0:
        return None
    else:
        return Node(max_exclusive - 1, range(max_exclusive - 1))

def occurs(target: int, ll: IntList):
    if ll is None:
        return False
    if ll.val == target:
        return True
    return occurs(target, ll.next)

# checks if the linked list has duplicate numbers
def has_dup(ll: IntList):
    if ll == None:
        return False
    if val_exists_in_list(ll.val, ll.next):
        return True
    return has_dup(ll.next)

#<- helper function for has_dup
def val_exists_in_list(value: int, nextNode: IntList) -> bool:
    if nextNode is None:
        return False
    if nextNode.val == value:
        return True
    return val_exists_in_list(value, nextNode.next)

#returns linked list where values are ascending.
def insertion_sort(ll: IntList, value: int) -> IntList:
    if ll == None:
        return Node(value, None)
    elif value > ll.val:
        return Node(ll.val, insertion_sort(ll.next, value))
    else:
        return Node(value, ll)  


class Tests(unittest.TestCase):

    def test_range(self):
        self.assertEqual(range(3), Node(0, Node(1, Node(2, None))))
        self.assertEqual(range(0), None)
        self.assertEqual(range(2), Node(0, Node(1, None)))

    def test_has_dup(self):
        self.assertFalse(has_dup(None))
        self.assertFalse(has_dup(Node(1, Node(2, None))))
        self.assertTrue(has_dup(Node(1, Node(2, Node(2, None)))))
        self.assertTrue(has_dup(Node(5, Node(5, Node(5, None)))))

    def test_range(self):
        self.assertEqual(range(0), None)
        self.assertEqual(range(-1), None)
        self.assertEqual(range(1), Node(0, None))
        self.assertEqual(range(2), Node(1, Node(0, None)))
        self.assertEqual(range(3), Node(2, Node(1, Node(0, None))))
        self.assertEqual(range(4), Node(3, Node(2, Node(1, Node(0, None)))))

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(None, 5), Node(5, None))
        self.assertEqual(insertion_sort(Node(7, None), 3), Node(3, Node(7, None)))
        self.assertEqual(insertion_sort(Node(2, None), 8), Node(2, Node(8, None)))

    def test_occurs(self):
        self.assertFalse(occurs(1, None))
        self.assertTrue(occurs(7, Node(7, None)))
        self.assertFalse(occurs(8, Node(7, None)))
        ll = Node(10, Node(20, Node(30, Node(40, None))))
        self.assertTrue(occurs(10, ll))
        self.assertTrue(occurs(30, ll))
        self.assertTrue(occurs(40, ll))
        self.assertFalse(occurs(999, ll))

if (__name__ == '__main__'):
    unittest.main()
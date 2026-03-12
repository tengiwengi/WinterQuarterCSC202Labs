import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

BinTree : TypeAlias = Union[None, "BTNode"]

@dataclass(frozen = True)
class BTNode: 
    val : Any
    left : BinTree
    right : BinTree

# example_btnode : BTNode = BTNode( 324, BTNode(345, None, None ), None )


def size(bt : BinTree ) -> int:
    if bt is None: 
        return 0
    else: 
        return 1 + size(bt.left) + size(bt.right)

def num_leaves(bt : BinTree) -> int:
    if bt is None: 
        return 0 
    
    if bt.left is None and bt.right is None:
        return 1 
    return num_leaves(bt.left) + num_leaves(bt.right)
    
def sum(bt : BinTree) -> int:
    if bt is None:
        return 0 
    else:
        return sum(bt.left) + sum(bt.right) + bt.val
    

def height(bt : BinTree) -> int:
    if bt is None: 
        return 0
    else : 
        left_height = height(bt.left)
        right_height = height(bt.right)
        return 1 + max(left_height, right_height)

def has_triple(bt : BinTree, val : int ) -> bool:
    if bt is None:
        return False
    else:
        #check the current node  
        if bt.val % 3 == 0:
            return True
        # checking the left and right subtrees
        return has_triple(bt.left, val) or has_triple(bt.right, val)        

def sub_one_map(bt : BinTree) -> BinTree:
    if bt is None: 
        return None
    else: 
        new_left = sub_one_map(bt.left)
        new_right = sub_one_map(bt.right)
        new_val = bt.val - 1
        return BTNode(new_val, new_left, new_right)




class TestCases(unittest.TestCase):
    
    tree2 : BinTree = BTNode(40, 
                        BTNode(9, None, None),
                        BTNode(8, None, None)
    )                        
    
    tree3 : BinTree = BTNode(40, 
                        BTNode(9, 
                               BTNode(50, None, None), 
                               BTNode(23, None, None)),
                        BTNode(8, None, None)
    )                                    

    tree4 : BinTree = BTNode(50, 
                             BTNode(40, 
                                    BTNode(39, None, None),
                                    BTNode(50, None, None)),
                             BTNode(39, 
                                    BTNode(1, None, None),
                                    BTNode(4, None, None)))
    
    
    def test_size(self):
        print("We are taking the size of the binary tree")
        self.assertEqual(size(self.tree2), 3)
        self.assertEqual(size(self.tree3), 5)
        self.assertEqual(size(self.tree4), 7)
    
    def test_num_leaves(self):
        print("We are now testing the amount of leaves within a Binary Tree")
        self.assertEqual(num_leaves(self.tree2), 2)
        self.assertEqual(num_leaves(self.tree3), 3)
        self.assertEqual(num_leaves(self.tree4), 4)
    
    def test_sum(self):
        print("We are now testing the sum of all the elements within the Binary Tree")
        self.assertEqual(sum(self.tree2), 57)
        self.assertEqual(sum(self.tree3), 130)
        self.assertEqual(sum(self.tree4), 223)
    
    def test_height(self):
        print("We are now testing the height of the Binary Tree")
        self.assertEqual(height(self.tree2), 2)
        self.assertEqual(height(self.tree3), 3)
        self.assertEqual(height(self.tree4), 3)

    def test_has_triple(self):
        print("We are now testing if the elemts in the Binary Tree ")
        self.assertEqual(has_triple(self.tree2, 3), True)
        self.assertEqual(has_triple(self.tree3, 3), True)
        self.assertEqual(has_triple(self.tree4, 3), True)
    
    def test_sub_one_map(self):
        print("We are now testing subtracting one from each element in the Binary Tree")
        self.assertEqual(sub_one_map(self.tree2), BTNode(39,
                                                        BTNode(8, None, None),
                                                        BTNode(7, None, None))
                                                        )
        self.assertEqual(sub_one_map(self.tree3), BTNode(39,
                                                         BTNode(8, 
                                                                BTNode(49, None, None),
                                                                BTNode(22, None, None)), 
                                                        BTNode(7, None, None)))
        self.assertEqual(sub_one_map(self.tree4), BTNode(49, 
                                                         BTNode(39, 
                                                                BTNode(38, None, None),
                                                                BTNode(49, None, None)),
                                                         BTNode(38, 
                                                                BTNode(0, None, None),
                                                                BTNode(3, None, None))))


if __name__ == "__main__":
    unittest.main()

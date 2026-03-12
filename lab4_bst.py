import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from typing import Callable

BinTree : TypeAlias = Union[None, "BTNode"]
comes_before = Callable[[Any,Any], bool] 

@dataclass(frozen = True)
class BTNode: 
    val : Any
    left : Any
    right : Any

@dataclass(frozen = True)
class BinarySearchTree: 
    func : comes_before
    bt : BinTree

def height(bt: BinTree) -> int:
    match bt:
        case None:
            return 0
        case BTNode(_, left, right):
            return 1 + max(height(left), height(right))

def is_empty(bst : BinarySearchTree) -> bool:
    if bst.bt is None:
        return True
    else:
        return False
    
def insert_helper(bt : BinTree, val : Any, comes_before: comes_before) -> BinTree:
    if bt is None:
        return BTNode(val, None, None)
    else:
        if comes_before(val, bt.val):
            #go left
            new_left = insert_helper(bt.left, val, comes_before)
            return BTNode(bt.val, new_left, bt.right)
        elif comes_before(val, bt.val):
            #go right
            new_right = insert_helper(bt.right, val, comes_before)
            return BTNode(bt.val, bt.left, new_right)
        else:
            return bt


def insert(bst : BinarySearchTree, val : Any) -> BinarySearchTree:
    new_bt = insert_helper(bst.bt, val, bst.func)
    return BinarySearchTree(bst.func, new_bt)    

def lookup(bst : BinarySearchTree, searchVal : int) -> bool:
    match bst.bt:
        case None:
            return False
        case BinTree(val, left, right):
            if not comes_before(searchVal, val) and not comes_before(val, searchVal):
                return True
            elif lookup(left) or lookup(right):
                return True
            else:
                return False

def find_min(bt: BinTree) -> Any:
    current = bt
    while current.left is not None:
        current = current.left
    return current.val

def delete(bst : BinarySearchTree, val : Any) -> BinarySearchTree:
    node = bst.bt
    func = bst.func
    
    if node is None:
        raise ValueError("The tree is empty")
    else:
        if func(val, node.val):
                #go left
                new_left = delete(BinarySearchTree(func, node.left), val)
                return BinarySearchTree(func, BTNode(node.val, new_left.bt, node.right))
        elif func(node.val, val):
                #go right
                new_right = delete(BinarySearchTree(func, node.right), val)
                return BinarySearchTree(func, BTNode(node.val, node.right, new_right.bt))
        else:
            if node.left is None and node.right is None:
                return BinarySearchTree(func, None)
            elif node.left is None:
                return BinarySearchTree(func, node.right)
            elif node.right is None:
                return BinarySearchTree(func, node.left)
        
            else:
                successor_val = find_min(node.right)
                new_right = delete(BinarySearchTree(func, node.right), successor_val)
                return BinarySearchTree(func, BTNode(successor_val, node.left, new_right.bt))
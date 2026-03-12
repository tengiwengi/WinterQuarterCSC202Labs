import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

MyList : TypeAlias = Union[None, "Pair"]

@dataclass(frozen=True)
class Pair:
    head: int
    tail: MyList                                                                                                                           

def length(list : MyList) -> int:                                                
    if list is None:
        return 0
    else:
        return 1 + length(list.tail)
    

def sum(list : MyList) -> int:
    if list is None: 
        return 0
    else: 
        return list.head + sum(list.tail)
    
def counter_greater_than( list : MyList, threshold : int) -> int:
     if list is None:
         return 0 
     else: 
         if list.head > threshold: 
                return 1 + counter_greater_than(list.tail, threshold)
         else: 
            return counter_greater_than(list.tail, threshold)


def find(list: MyList, value: int, index: int) -> Union[int, None]:
    if list is None:
        return None
    if list.head == value:
        return index
    return (find(list.tail, value, index + 1))

          
def sub_one_map(list : MyList) -> MyList:
    if list is None: 
        return None
    else: 
        return Pair(list.head - 1, sub_one_map(list.tail))

def insert(list : MyList, value : int) -> MyList: 
    if list is None:
        return None
    else: 
        if list.head >= value:
            return Pair(value, list)
        return Pair(list.head, insert(list.tail, value))



        

# atleast 3 testcases per function

class TestCase(unittest.TestCase): 
    def test_length(self): 
        print("We are testing the length of the linked list")
        self.assertEqual(length(Pair(2, Pair(10, Pair(4, None)))), 3)
        self.assertEqual(length(Pair(3, Pair(4, Pair(50, Pair(60, Pair(20, None)))))), 5)
        self.assertEqual(length(Pair(10, Pair(23, Pair(10 , Pair(2, None))))), 4)
        
    def test_sum(self):
        print("We are testing the sum of the linked list")    
        self.assertEqual(sum(Pair(2, Pair(10, Pair(4, None)))), 16)
        self.assertEqual(sum(Pair(10, Pair(30, Pair(50, Pair(70, None))))), 160)
        self.assertEqual(sum(Pair(2, Pair(5, Pair(10, Pair(50, None))))), 67)

    def test_counter_greater_than(self):
        print("We are testing the counter greater than function")
        self.assertEqual(counter_greater_than(Pair(2, Pair(10, Pair(4, None))), 3), 2)
        self.assertEqual(counter_greater_than(Pair(10, Pair(30, Pair(50, Pair(41, None)))), 20), 3)
        self.assertEqual(counter_greater_than(Pair(51, Pair(102, Pair(0, Pair(4, None)))), 39), 2)

    def test_find(self):
        print("We are testing the find function")
        self.assertEqual(find(Pair(2, Pair(10, Pair(5, Pair(10, Pair(20, Pair(50, None)))))), 10, 0), 1)
        self.assertEqual(find(Pair(4, Pair(100, Pair(68, Pair(2300, Pair(0, Pair(4000, Pair(400, None))))))), 0, 0), 4)
        self.assertEqual(find(Pair(100, Pair(230, Pair(421, Pair(5000, Pair(4321, None))))), 5000, 0), 3)

    def test_sub_one_map(self):
        print("We are testing if we can subtract one from each element in the linked list")
        self.assertEqual(sub_one_map(Pair(2, Pair(3, Pair(4, None)))), (Pair(1, Pair(2, Pair(3, None)))))
        self.assertEqual(sub_one_map(Pair(10, Pair(20, Pair(30, Pair(40, None))))), (Pair(9, Pair(19, Pair(29, Pair(39, None))))))
        self.assertEqual(sub_one_map(Pair(5, Pair(15, Pair(25, None)))), (Pair(4, Pair(14, Pair(24, None)))))

    def test_insert(self):
        print("We are testing the insert function")
        self.assertEqual(insert(Pair(2, Pair(4, Pair(10, None))), 5), (Pair(2, Pair(4, Pair(5, Pair(10, None))))))
        self.assertEqual(insert(Pair(1, Pair(2, Pair(3, Pair(4, Pair(6, None))))), 5), (Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, Pair(6, None))))))))
        self.assertEqual(insert(Pair(5, Pair(10, Pair(15, Pair(20, Pair(30, None))))), 25), (Pair(5, Pair(10, Pair(15, Pair(20, Pair(25, Pair(30, None))))))))

if __name__ == "__main__":
    unittest.main()




import sys
import unittest
from typing import *
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt
import numpy as np
import random
import time
sys.setrecursionlimit(10**6)
from bst import *

TREES_PER_RUN : int = 10000

# Creates graph averaging tree size vs tree height
def graph_average_height(n_max: int) -> None:
    n_values: List[int] = [int(i) for i in np.linspace(0, n_max, 50)]
    
    average_heights: List[float] = []
    print(f"Calculating average heights for {len(n_values)} different N values")
    for i, n in enumerate(n_values):        
        total_height = 0
        for _ in range(TREES_PER_RUN):
            bst = random_tree(n)
            total_height += height(bst.bt)
        
        avg_height = total_height / TREES_PER_RUN
        average_heights.append(avg_height)
    
    x_numpy: np.ndarray = np.array([float(n) for n in n_values])
    y_numpy: np.ndarray = np.array(average_heights)
    
    plt.plot(x_numpy, y_numpy, label='Graph')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"tree height vs tree size")
    plt.grid(True)
    plt.legend()
    plt.show()

# Creates a graph of average insertion time (y-axis) as a function of N (x-axis).
def graph_insertion_time(n_max: int) -> None:
    n_values: List[int] = [int(i) for i in np.linspace(1, n_max, 50)]
    n_values = sorted(list(set(n_values)))
    if len(n_values) < 50:
        n_values = [int(i) for i in np.linspace(0, n_max, min(50, n_max + 1))]
        n_values = sorted(list(set(n_values)))
    
    average_times: List[float] = []
    
    for i, n in enumerate(n_values):
        trees: List[BinarySearchTree] = []
        random_values: List[float] = []
        for _ in range(TREES_PER_RUN):
            trees.append(random_tree(n))
            random_values.append(random.random())
        start_time = time.perf_counter()
        for bst, val in zip(trees, random_values):
            insert(bst, val)
        end_time = time.perf_counter()
        
        total_time = end_time - start_time
        avg_time = total_time / TREES_PER_RUN
        average_times.append(avg_time)
    
    x_numpy: np.ndarray = np.array([float(n) for n in n_values])
    y_numpy: np.ndarray = np.array(average_times)
    
    # Create the graph
    plt.plot(x_numpy, y_numpy, label='Average Insertion Time')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Average insertion time vs tree size")
    plt.grid(True)
    plt.legend()
    plt.show()

# Generates a random tree with size n
def random_tree(n: int) -> BinarySearchTree:
    def standard_less_than(a: float, b: float) -> bool:
        return a < b
    
    bst = BinarySearchTree(standard_less_than, None)
    for _ in range(n):
        random_float = random.random()
        bst = insert(bst, random_float)
    
    return bst

if (__name__ == '__main__'):
    n_max = 50
    graph_average_height(n_max)
    n_max=30
    graph_insertion_time(n_max)
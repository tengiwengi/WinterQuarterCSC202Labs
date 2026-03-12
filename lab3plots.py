from typing import *
import unittest
import math
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
import functions


sys.setrecursionlimit(10**9)

def generate_n_values(n_max: int, num_points: int = 15) -> List[int]:
    n_values = np.linspace(1, n_max, num_points)
    return [int(round(n)) for n in n_values]


def time_function_call(func: Callable, *args, **kwargs) -> float:
    start_time: float = time.perf_counter()
    func(*args, **kwargs) #Calls function twice
    end_time: float = time.perf_counter()
    return end_time - start_time


def average_runtime(func: Callable, test_input: Any, num_runs: int = 4) -> float:
    total_time = 0.0
    for _ in range(num_runs):
        total_time += time_function_call(func, test_input)
    return total_time / num_runs


def create_worst_case_input_has_dup(n: int) -> functions.IntList:
    return functions.range(n)


def create_worst_case_graph():
    n_max = 6500
    print(f"Using n_max = {n_max}")
    print(f"Collecting data for 15 points from 1 to {n_max}...\n")
    
    n_values = generate_n_values(n_max, 15)
    runtimes = []
    
    for i, n in enumerate(n_values, 1):
        print(f"{i}/15 - Testing n={n}...", end=" ")
        test_input = create_worst_case_input_has_dup(n)
        avg_time = average_runtime(functions.has_dup, test_input, num_runs=4)
        runtimes.append(avg_time)
        print(f"{avg_time:.4f} seconds")
    
    plt.plot(n_values, runtimes, 'b-o', linewidth=2, markersize=6)
    plt.xlabel("N (Input Size)")
    plt.ylabel("Time (seconds)")
    plt.title("Worst-Case Time Complexity: has_dup()")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.tight_layout()
    plt.show()
    
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    print(f"Function: has_dup")
    print(f"Worst-case scenario: No duplicates in list")
    print(f"n_max: {n_max}")
    print(f"Min runtime: {min(runtimes):.4f} seconds (at n={n_values[runtimes.index(min(runtimes))]})")
    print(f"Max runtime: {max(runtimes):.4f} seconds (at n={n_values[runtimes.index(max(runtimes))]})")
    print(f"Average runtime: {sum(runtimes)/len(runtimes):.4f} seconds")


def example_graph_creation() -> None:
    def f_to_graph(x: float) -> float:
        return math.log2(x) + 5.0

    x_coords: List[float] = [float(i) for i in range(1, 100)]
    y_coords: List[float] = [f_to_graph(x) for x in x_coords]
    
    x_numpy: np.ndarray = np.array(x_coords)
    y_numpy: np.ndarray = np.array(y_coords)
    
    plt.plot(x_numpy, y_numpy, label="log_2(x)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Example Graph")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    create_worst_case_graph()
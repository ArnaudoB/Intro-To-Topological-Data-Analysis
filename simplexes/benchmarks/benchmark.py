# In this file we benchmark our three functions simplexes, simplexes_parallelism and simplexes_kdtree_parallelism
# for low values of n (2 <= n < 100) by comparing their execution time.

import time
import numpy as np
import matplotlib.pyplot as plt
from simplexes.simplexes import simplexes
from simplexes.simplexes_parallelized import simplexes_parallelism
from simplexes.simplexes_with_kdtree_parallelism import simplexes_kdtree_parallelism

def generate_points(d, n=20):
    """Generate n points in [0,1]^d uniformly at random."""
    return np.random.rand(n, d).tolist()

def benchmark_function(func, d, k, l, M=2, n=20):
    """Measure average execution time of a function over M trials."""
    total_time = 0
    for _ in range(M):
        P = generate_points(d, n)
        start = time.time()
        func(P, l, k)
        total_time += time.time() - start
    return total_time / M

if __name__ == '__main__':
    d=5 # Dimension of the points
    n_values=list(range(2, 100))
    k=30 # Maximum dimension of the simplexes
    l=0.2 # Filtration limit
    M=10 # Number of trials
    exec_times_naive = []
    exec_times_parallel = []
    exec_times_kdtree_parallel = []

    for n in n_values:
        time_naive = benchmark_function(simplexes, d, k, l, M, n)
        time_parallel = benchmark_function(simplexes_parallelism, d, k, l, M, n)
        time_kdtree_parallel = benchmark_function(simplexes_kdtree_parallelism, d, k, l, M, n)
        exec_times_naive.append(time_naive)
        exec_times_parallel.append(time_parallel)
        exec_times_kdtree_parallel.append(time_kdtree_parallel)
        if n % 10 == 0:
            print(f"n={n}, Naive Simplexes: {time_naive:.3f}s, Parallel Simplexes: {time_parallel:.3f}s, Parallel Simplexes with KDTree: {time_kdtree_parallel:.3f}s")

    # Plot execution times
    plt.plot(n_values, exec_times_naive, label="Simplexes", marker='o')
    plt.plot(n_values, exec_times_parallel, label="Parallel Simplexes", marker='s')
    plt.plot(n_values, exec_times_kdtree_parallel, label="Parallel Simplexes with KDTree", marker='x')
    plt.xlabel("Number of points n")
    plt.ylabel("Execution Time (s)")
    plt.title("Execution Time vs. Number of Points")
    plt.legend()
    plt.grid()
    plt.savefig("benchmark_simplexes_vs_parallelizedsimplexes_vs_parallelizedkdtreesimplexes_d5_k30_l02_low_values_of_n.png")
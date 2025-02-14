# In this file, we benchmark our three functions simplexes, simplexes_parallelism and simplexes_kdtree_parallelism
# for medium values of n (50 <= n < 200) by comparing their execution time.

from simplexes.benchmarks.benchmark import benchmark_function
import matplotlib.pyplot as plt
from simplexes.simplexes import simplexes
from simplexes.simplexes_parallelized import simplexes_parallelism
from simplexes.simplexes_with_kdtree_parallelism import simplexes_kdtree_parallelism

if __name__ == '__main__' :
    d=5 # Dimension of the points
    n_values=list(range(50, 200))
    k=30 # Maximum dimension of the simplexes
    l=0.2 # Filtration limit
    M=5 # Number of trials
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
    plt.savefig("benchmark_simplexes_vs_parallelizedsimplexes_vs_parallelizedkdtreesimplexes_d5_k30_l02_medium_values_of_n.png")
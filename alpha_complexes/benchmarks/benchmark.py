from simplexes.benchmarks.benchmark import benchmark_function
import matplotlib.pyplot as plt
from alpha_complexes.alpha_simplexes import alpha_simplexes
from alpha_complexes.alpha_simplexes_optimized import alpha_simplexes_optimized

if __name__ == '__main__' :
    d=5 # Dimension of the points
    n_values=list(range(2, 150))
    k=30 # Maximum dimension of the simplexes
    l=0.2 # Filtration limit
    M=5 # Number of trials
    exec_times_naive = []
    exec_times_optimized = []

    for n in n_values:
        time_naive = benchmark_function(alpha_simplexes, d, k, l, M, n)
        time_optimized= benchmark_function(alpha_simplexes_optimized, d, k, l, M, n)
        exec_times_naive.append(time_naive)
        exec_times_optimized.append(time_optimized)
        if n % 50 == 0:
            print(f"n={n}, Naive α-Simplexes: {time_naive:.3f}s, Optimized α-Simplexes: {time_optimized:.3f}s")

    # Plot execution times
    plt.plot(n_values, exec_times_naive, label="Naive α-Simplexes", marker='o')
    plt.plot(n_values, exec_times_optimized, label="Optimized α-Simplexes", marker='s')
    plt.xlabel("Number of points n")
    plt.ylabel("Execution Time (s)")
    plt.title("Execution Time vs. Number of Points")
    plt.legend()
    plt.grid()
    plt.savefig("benchmark_alpha_simplexes_vs_alpha_simplexes_optim_d5_k30_l02.png")
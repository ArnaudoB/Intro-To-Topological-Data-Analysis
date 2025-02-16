import os
from naive_simplexes.naive_simplexes import naive_simplexes

def plot_simplexes(P, simplexes, output_file="plot3d"):
    """
    Given a list of points and a list of simplexes (tuples of points), plots them.
    """
    
    with open('coord.txt', 'w') as f:
        for point in P:
            f.write(f"{point[0]} {point[1]} {point[2]}\n")
    
    with open('cplx.txt', 'w') as s:
        for simplex in simplexes:
            s.write(" ".join(map(str, simplex)) + "\n")
    
    os.system(f"./plot_simplexes/sc.py --complex cplx.txt --coordinates coord.txt --output {output_file} plot3d")

if __name__ == '__main__':
    # Comparison of the simplexes of the Cech and alpha complexes of a random set of points in R^3
    import numpy as np
    P = np.random.rand(5, 3)
    from simplexes.simplexes import simplexes
    from alpha_complexes.alpha_simplexes import alpha_simplexes
    dic = simplexes(P, 0.5, 3)
    simplexess = list(dic.keys())
    dic2 = alpha_simplexes(P, 0.5, 3)
    simplexess2 = list(dic2.keys())
    plot_simplexes(P, simplexess, "plot3d_cech_n5_k3_l05")
    plot_simplexes(P, simplexess2, "plot3d_alpha_n5_k3_l05")


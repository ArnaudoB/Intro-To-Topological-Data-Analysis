# Here, we write some tests to our alpha_simplexes function by comparing the results of our function to the results given by the gudhi's library.

import gudhi as gd
import numpy as np
from alpha_complexes.alpha_simplexes import alpha_simplexes
from plot_simplexes.plot_simplexes import plot_simplexes

def test_alpha_simplices():

    print("Testing for a set of 1 point in 3D... \n")

    P = [[0,0,0]]
    dic = alpha_simplexes(P, 1, 0)
    print(dic)
    assert list(dic.keys()) == [(0,)] and np.allclose(list(dic.values()), [0], rtol=1e-5, atol=1e-5), "Test failed"

    print("Test passed \n")
    print("-------------------- \n")


    print("Testing for a set of 2 points in 3D... \n")

    P = [[0,0,0], [1,0,0]]
    dic = alpha_simplexes(P, 1, 1)
    tuples = sorted(list(dic.keys()), key=tuple)
    filtrations = sorted(list(dic.values()))
    assert tuples == [(0,), (0, 1), (1,)] and np.allclose(filtrations, [0, 0, 0.5], rtol=1e-5, atol=1e-5), "Test failed"

    print("Test passed \n")
    print("-------------------- \n")


    print("Testing for a set of 3 points in 3D... \n")

    P = [[0,0,0], [1,0,0], [0,1,0]]
    dic = alpha_simplexes(P, 1, 2)

    alpha_complex = gd.AlphaComplex(points=P)
    simplex_tree = alpha_complex.create_simplex_tree(max_alpha_square=np.inf)
    simplices = simplex_tree.get_simplices()
    filtered_simplices = [
    simplex for simplex in simplices
    if len(simplex[0]) <= 3 and simplex_tree.filtration(simplex[0]) <= 1 # List of tuples (simplex (as a list), filtration value) WATCH OUT: in Gudhi, the filtration value is squared
    ]
    assert len(dic) == len(filtered_simplices), "Test failed"
    flag = True
    for simplex in filtered_simplices:
        if tuple(simplex[0]) not in dic.keys():
            flag = False
            break
        if not np.allclose(dic[tuple(simplex[0])]**2, simplex_tree.filtration(simplex[0]), rtol=1e-5, atol=1e-5):
            flag = False
            break
    assert flag, "Test failed"

    print("Test passed \n")
    print("-------------------- \n")


    print("Testing for a set of 10 points in 3D... \n")

    P = np.random.rand(10, 3)
    dic = alpha_simplexes(P, 0.5, 5)
    alpha_complex = gd.AlphaComplex(points=P)

    simplex_tree = alpha_complex.create_simplex_tree(max_alpha_square=np.inf)
    simplices = simplex_tree.get_simplices()
    filtered_simplices = [
    simplex for simplex in simplices
    if len(simplex[0]) <= 6 and simplex_tree.filtration(simplex[0]) <= 0.25 # List of tuples (simplex (as a list), filtration value) WATCH OUT: in Gudhi, the filtration value is squared
    ]
    print(len(dic))
    print(len(filtered_simplices))
    assert len(dic) == len(filtered_simplices), "Test failed"
    flag = True
    for simplex in filtered_simplices:
        if tuple(simplex[0]) not in dic.keys():
            flag = False
            break
        if not np.allclose(dic[tuple(simplex[0])]**2, simplex_tree.filtration(simplex[0]), rtol=1e-5, atol=1e-5):
            flag = False
            break
    assert flag, "Test failed"
    print("Test passed \n")
    plot_simplexes(P, [simplex[0] for simplex in filtered_simplices])
    print("-------------------- \n")

    print("All tests passed")

if __name__ == '__main__':
    test_alpha_simplices()
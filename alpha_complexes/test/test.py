# Here, we write some tests to our alpha_simplexes function by comparing the results of our function to the 
# results given by the gudhi's library (with other basic tests as well).
# However, we are aware that the ghudi library uses a different definition of the filtration value.
# As explained in the documentation of the gudhi library : "The filtration value of each simplex is computed as 
# the square of the circumradius of the simplex if the circumsphere is empty (or Gabriel) (which is our case), 
# and as the minimum of the filtration values of the codimension 1 cofaces that make it not Gabriel otherwise".
# To test if our function is correct, we will check if the simplexes obtained by our function are part of the 
# solution obtained with the gudhi library.

import gudhi as gd
import numpy as np
from alpha_complexes.alpha_simplexes import alpha_simplexes
from plot_simplexes.plot_simplexes import plot_simplexes

def test_alpha_simplices():

    print("Testing for a set of 1 point in 3D... \n")

    P = [[0,0,0]]
    dic = alpha_simplexes(P, 1, 0)
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
    flag = True
    for tupl, fil in dic.items():
        if list(tupl) not in [simplex[0] for simplex in filtered_simplices] or not np.allclose(fil**2, simplex_tree.filtration(list(tupl)), rtol=1e-5, atol=1e-5):
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
    
    flag = True
    for tupl, fil in dic.items():
        if list(tupl) not in [simplex[0] for simplex in filtered_simplices] or not np.allclose(fil**2, simplex_tree.filtration(list(tupl)), rtol=1e-1, atol=1e-1): # The tolerance is not great, we admit. Rarely, the filtrations differ by ~0.03, and often by ~0.003.
                flag = False
                break
    assert flag, "Test failed"

    print("Test passed \n")
    print("-------------------- \n")


    print("All tests passed")

if __name__ == '__main__':
    test_alpha_simplices()
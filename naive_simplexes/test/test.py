# Tests the function naive_simplexes

import numpy as np
from naive_simplexes.naive_simplexes import naive_simplexes
from plot_simplexes.plot_simplexes import plot_simplexes

def test_naive_simplexes():

    print("Testing for a set of 1 point in 3D... \n")
    P = [[0,0,0]]
    dic = naive_simplexes(P, 0)
    assert list(dic.keys()) == [(0,)] and np.allclose(list(dic.values()), [0], rtol=1e-5, atol=1e-5), "Test failed"
    print("Test passed \n")
    print("-------------------- \n")

    print("Testing for a set of 2 points in 3D... \n")
    P = [[0,0,0], [1,0,0]]
    dic = naive_simplexes(P, 1)
    tuples = sorted(list(dic.keys()), key=tuple)
    filtrations = sorted(list(dic.values()))
    assert tuples == [(0,), (0, 1), (1,)] and np.allclose(filtrations, [0, 0, 0.5], rtol=1e-5, atol=1e-5), "Test failed"
    print("Test passed \n")
    print("-------------------- \n")

    print("Testing for a set of 3 points in 3D... \n")
    P = [[0,0,0], [1,0,0], [0,1,0]]
    dic = naive_simplexes(P, 2)
    tuples = sorted(list(dic.keys()), key=tuple)
    filtrations = sorted(list(dic.values()))
    assert tuples == [(0,), (0, 1), (0, 1, 2), (0, 2), (1,), (1, 2), (2,)] and np.allclose(filtrations, [0, 0, 0, 0.5, 0.5, np.sqrt(2)/2, np.sqrt(2)/2], rtol=1e-5, atol=1e-5), "Test failed"
    print("Test passed \n")
    plot_simplexes(P, tuples)
    print("-------------------- \n")

    print("Testing for a set of 4 points in 3D... \n")
    P = [[0,0,0], [1,0,0], [0,1,0], [0,0,1]]
    dic = naive_simplexes(P, 3)
    tuples = sorted(list(dic.keys()), key=tuple)
    filtrations = sorted(list(dic.values()))
    assert (tuples==[(0,), (0, 1), (0, 1, 2), (0, 1, 2, 3), (0, 1, 3), (0, 2), (0, 2, 3), (0, 3), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)] 
            and np.allclose(filtrations, [0, 0, 0, 0, 0.5, 0.5, 0.5, np.sqrt(2)/2, np.sqrt(2)/2, np.sqrt(2)/2, np.sqrt(2)/2, np.sqrt(2)/2, np.sqrt(2)/2, 0.8165, 0.8165])), "Test failed"
    print("Test passed \n")
    plot_simplexes(P, tuples)
    print("-------------------- \n")

    print("All tests passed")

if __name__ == '__main__':
    test_naive_simplexes()
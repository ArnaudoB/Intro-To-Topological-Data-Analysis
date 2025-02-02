from simplexes.simplexes import simplexes
from plot_simplexes.plot_simplexes import plot_simplexes
import numpy as np

def test_simplexes():
    """
    Writes some basic tests for the simplexes function.
    """

    print("Testing for a set of 1 point in 3D... \n")

    P = [[0,0,0]]
    dic = simplexes(P, 1, 0)
    assert list(dic.keys()) == [(0,)] and np.allclose(list(dic.values()), [0], rtol=1e-5, atol=1e-5), "Test failed"

    # Testing invalid filtration limit
    dic = simplexes(P, -1, 0)
    assert list(dic.keys()) == [] and list(dic.values()) == [], "Test failed"

    print("Test passed \n")
    print("-------------------- \n")


    print("Testing for a set of 2 points in 3D... \n")

    P = [[0,0,0], [1,0,0]]
    dic = simplexes(P, 0.2, 1)
    sorted_items = sorted(dic.items())
    tuples = [item[0] for item in sorted_items]
    filtrations = [item[1] for item in sorted_items]
    assert tuples == [(0,), (1,)] and np.allclose(filtrations, [0, 0], rtol=1e-5, atol=1e-5), "Test failed"

    print("Test passed \n")
    print("-------------------- \n")


    print("Testing for a set of 3 points in 3D... \n")

    P = [[0,0,0], [1,0,0], [0,1,0]]
    dic = simplexes(P, 0.6, 2)
    sorted_items = sorted(dic.items())
    tuples = [item[0] for item in sorted_items]
    filtrations = [item[1] for item in sorted_items]
    assert tuples == [(0,), (0, 1), (0, 2), (1,), (2,)] and np.allclose(filtrations, [0, 0.5, 0.5, 0, 0], rtol=1e-5, atol=1e-5), "Test failed"

    print("Test passed \n")
    print("-------------------- \n")


    print("Testing for a set of 4 points in 3D... \n")

    P = [[0,0,0], [1,0,0], [0,1,0], [0,0,1]]
    dic = simplexes(P, 0.75, 3)
    sorted_items = sorted(dic.items())
    tuples = [item[0] for item in sorted_items]
    filtrations = [item[1] for item in sorted_items]
    assert (tuples==[(0,), (0, 1), (0, 1, 2), (0, 1, 3), (0, 2), (0, 2, 3), (0, 3), (1,), (1, 2), (1, 3), (2,), (2, 3), (3,)]
            and np.allclose(filtrations, [0, 0.5, np.sqrt(2)/2, np.sqrt(2)/2, 0.5, np.sqrt(2)/2, 0.5, 0, np.sqrt(2)/2, np.sqrt(2)/2, 0, np.sqrt(2)/2, 0], rtol=1e-5, atol=1e-5)), "Test failed"
    
    print("Test passed \n")
    print("-------------------- \n")


    print("All tests passed")

if __name__ == '__main__':
    test_simplexes()
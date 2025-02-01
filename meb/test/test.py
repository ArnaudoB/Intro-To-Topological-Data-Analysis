# Tests the MEB function

import numpy as np
from meb.meb import MEB
from meb.plot_sphere_points import plot_sphere_points

def test_MEB():

    print("Testing a single point in 2D... \n")
    P = [[0,0]]
    c, r = MEB(P)
    plot_sphere_points(P, c, r, "test_MEB_single_point_2D.png")
    assert np.allclose(c, [0, 0], rtol=1e-5, atol=1e-5) and np.allclose(r, 0, rtol=1e-5, atol=1e-5), "Test failed"
    print("Test passed \n")
    print("-------------------- \n")

    print("Testing 2 points in 2D... \n")
    P = [[0,0], [1,0]]
    c, r = MEB(P)
    plot_sphere_points(P, c, r, "test_MEB_2_points_2D.png")
    assert np.allclose(c, [0.5, 0], rtol=1e-5, atol=1e-5) and np.allclose(r, 0.5, rtol=1e-5, atol=1e-5), "Test failed"
    print("Test passed \n")
    print("-------------------- \n")

    print("Testing 3 aligned points in 2D... \n")
    P = [[0,0], [0,1], [0,2]]
    c, r = MEB(P)
    plot_sphere_points(P, c, r, "test_MEB_3_aligned_points_2D.png")
    assert np.allclose(c, [0, 1], rtol=1e-5, atol=1e-5) and np.allclose(r, 1, rtol=1e-5, atol=1e-5), "Test failed"
    print("Test passed \n")
    print("-------------------- \n")

    print("Testing 3 points in 2D... \n")
    P = [[0,0], [1,0], [0,1]]
    c, r = MEB(P)
    plot_sphere_points(P, c, r, "test_MEB_3_points_2D.png")
    assert np.allclose(c, [0.5, 0.5], rtol=1e-5, atol=1e-5) and np.allclose(r, np.sqrt(2)/2, rtol=1e-5, atol=1e-5), "Test failed"
    print("Test passed \n")
    print("-------------------- \n")

    print("Testing 1 points in 3D... \n")
    P = [[0,0,0]]
    c, r = MEB(P)
    plot_sphere_points(P, c, r, "test_MEB_single_point_3D.png")
    assert np.allclose(c, [0, 0, 0], rtol=1e-5, atol=1e-5) and np.allclose(r, 0, rtol=1e-5, atol=1e-5), "Test failed"
    print("Test passed \n")
    print("-------------------- \n")

    print("Testing 2 points in 3D... \n")
    P = [[0,0,0], [1,0,0]]
    c, r = MEB(P)
    plot_sphere_points(P, c, r, "test_MEB_2_points_3D.png")
    assert np.allclose(c, [0.5, 0, 0], rtol=1e-5, atol=1e-5) and np.allclose(r, 0.5, rtol=1e-5, atol=1e-5), "Test failed"
    print("Test passed \n")
    print("-------------------- \n")

    print("Testing 3 aligned points in 3D... \n")
    P = [[0,0,0], [0,1,0], [0,2,0]]
    c, r = MEB(P)
    plot_sphere_points(P, c, r, "test_MEB_3_aligned_points_3D.png")
    assert np.allclose(c, [0, 1, 0], rtol=1e-5, atol=1e-5) and np.allclose(r, 1, rtol=1e-5, atol=1e-5), "Test failed"
    print("Test passed \n")
    print("-------------------- \n")

    print("Testing 3 points in 3D... \n")
    P = [[0,0,0], [1,0,0], [0,1,0]]
    c, r = MEB(P)
    plot_sphere_points(P, c, r, "test_MEB_3_points_3D.png")
    assert np.allclose(c, [0.5, 0.5, 0], rtol=1e-5, atol=1e-5) and np.allclose(r, np.sqrt(2)/2, rtol=1e-5, atol=1e-5), "Test failed"
    print("Test passed \n")
    print("-------------------- \n")

    print("Testing 10 points in 3D... \n")
    points = []
    for _ in range(4): # We take a basis of four points lying on the unit sphere
        random_vect = np.random.randn(3)
        random_vect /= np.linalg.norm(random_vect)
        points.append(random_vect)
    # We add 6 random points inside the sphere
    eps = 1e-3
    for _ in range(6):
        random_vect = np.random.randn(3)
        random_vect /= (np.linalg.norm(random_vect) + eps)
        points.append(random_vect)
    # The result should be the MEB of the basis, i.e. the unit sphere
    c, r = MEB(points)
    plot_sphere_points(points, c, r, "test_MEB_10_points_3D.png")
    assert np.allclose(c, [0, 0, 0], rtol=1e-5, atol=1e-5) and np.allclose(r, 1, rtol=1e-5, atol=1e-5), "Test failed"
    print("Test passed \n")
    print("-------------------- \n")

    print("All tests passed")

if __name__ == '__main__':
    test_MEB()
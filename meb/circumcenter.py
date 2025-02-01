import numpy as np

def circumcenter(points):
    points = np.array(points)
    n = len(points)

    # Trivial cases
    if n == 0:
        return None
    if n == 1:
        return points[0]
    if n == 2:
        return 0.5 * (points[0] + points[1])

    A = np.hstack((2.0 * (points - points[0]), np.ones((n, 1))))
    b = np.sum(points ** 2 - points[0] ** 2, axis=1)

    theta = np.linalg.lstsq(A, b, rcond=None)[0]

    center = theta[:-1]
    return center
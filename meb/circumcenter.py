import numpy as np

# def circumcenter(points):

#     points = np.array(points)
#     n = len(points)

#     # Potentially pathological cases

#     if n == 0:
#         return None
    
#     if n == 1:
#         return points[0]
    
#     if n == 2:
#         return (points[0] + points[1])/2

#     A = np.zeros((n, n))
#     b = np.zeros(n)
#     for i in range(n-1):
#         for j in range(n):
#             A[i, j] = np.dot(points[j], points[0] - points[i+1])
#     for j in range(n):
#         A[n-1,j]=1

#     for i in range(n-1):
#         b[i] = (np.linalg.norm(points[0])**2 - np.linalg.norm(points[i+1])**2)/2
#     b[n-1]=1

#     theta  = scipy.linalg.pinv(A)@b

#     circumcenter = np.zeros(points.shape[1])
#     for i in range(n):
#         circumcenter += theta[i]*points[i]
#     return circumcenter

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
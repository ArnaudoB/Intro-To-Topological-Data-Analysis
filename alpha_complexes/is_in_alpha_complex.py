from meb.circumcenter import circumcenter
import numpy as np

def is_in_alpha_complex(P, simplex):
    """
    Tests if a simplex is in the alpha complex of a set of points, and if so, returns the radius of the circumscribed ball.
    """
    c = circumcenter(simplex)
    r = np.linalg.norm(c - simplex[0])
    for p in P :
        if np.linalg.norm(c - p) < r:
            return False, None
    return True, r
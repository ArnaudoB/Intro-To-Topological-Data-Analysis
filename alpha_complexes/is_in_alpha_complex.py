from meb.circumcenter import circumcenter
import numpy as np

def is_in_alpha_complex(P, simplex):
    """
    Tests if a simplex is in the alpha complex of a set of points, and if so, returns the radius of the circumscribed ball.
    """
    c = circumcenter(simplex)
    r = np.linalg.norm(c - simplex[0])
    # if np.linalg.norm(c - c2) > 1e-10:
    #     print(f"r = {r} and r2 = {r2} and my point {c} and the other {c2} are at distance {np.linalg.norm(c - c2)}")
    for p in P :
        if not any(np.array_equal(p, s) for s in simplex) and np.linalg.norm(c - p) <= r + 1e-10:
            #print(f"r = {r} and the point {p} is at distance {np.linalg.norm(c - p)}") 
            return False, None
    return True, r
from meb.circumcenter import circumcenter
import numpy as np

def sphere_alpha(P, S):
    """
    Returns the center and the radius of the minimum enclosing ball of a set of points.
    """

    # Implementing the Welzl algorithm
    def welzl(P, R):
        """
        We use Welzl's algorithm to compute the basis of the ball.
        """

        if len(P) == 0 or len(R) == len(P[0])+1: # dimension + 1
            return R

        P = np.random.permutation(P)
        p = P[0]
        P_wo_p = P[1:]
        R_ = welzl(P_wo_p, R)

        if len(R_) != 0:
            c = circumcenter(R_)
            r = np.linalg.norm(c-R_[0])

            if np.linalg.norm(p-c) >= r:
                return R_

        return welzl(P_wo_p, R+[p])

    # Returning results after running Welzl
    P_wo_S = [p for p in P if not any(np.array_equal(p, s) for s in S)]
    R = welzl(P_wo_S, S)
    c = circumcenter(R)
    r = np.linalg.norm(c-R[0])
    if (all(np.linalg.norm(p - c) >= r for p in P) and
        all(np.isclose(np.linalg.norm(s - c), r) for s in S)):
        return c, r
    else :
        return None
    
def is_in_alpha_complex(P, simplex) :
  res = sphere_alpha(P, simplex)
  if res is not None :
    c, r = res
    return True, r
  return False, None
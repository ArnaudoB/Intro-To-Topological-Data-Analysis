import numpy as np
from meb.circumcenter import circumcenter

def MEB(P):
    """
    Returns the center and the radius of the minimum enclosing ball of a set of points.
    """
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

            if np.linalg.norm(p-c) < r:
                return R_
        
        return welzl(P_wo_p, R+[p])
    
    R = welzl(P, [])
    c = circumcenter(R)
    r = np.linalg.norm(c-R[0])
    return c, r
from concurrent.futures import ProcessPoolExecutor, as_completed
from meb.meb import MEB
import numpy as np

def diam(P, p):
  """
  Computes the diameter of a set of points P with respect to a point p.
  """
  p=np.array(p)
  if not P:
    return 0
  return max([np.linalg.norm(p1-p) for p1 in P])

def simplexes_parallelism(P, l, k):
    """
    Given a set P of in R^d, enumerates the simplexes of dimension at most k (hence having at most
    k + 1 vertices) and having a filtration value at most l of the Čech complex of P using parallelism to speed up the computations of the MEBs.
    """
    n = len(P)
    lim = min(k, n) + 1
    tuples = []
    filtrations = []
    simplex=[]
    
    def backtrack(idx, curpoints, ind_curpoints, diameter):
        """
        Recursive backtracking function to find simplexes with filtration < l.
        """
        nonlocal n, tuples, filtrations
        if len(curpoints) > lim or diameter >= 2*l: # Simplex with more than k + 1 vertices
            return

        if idx == n:
            if curpoints and diameter < 2*l:
                tuples.append(ind_curpoints)
                simplex.append(curpoints)
            return

        new_ind_curpoints = ind_curpoints + [idx]
        new_curpoints = curpoints + [P[idx]]
        new_diameter = max(diameter, diam(curpoints, P[idx]))
        backtrack(idx + 1, new_curpoints, new_ind_curpoints, new_diameter)

        backtrack(idx + 1, curpoints, ind_curpoints, diameter)

    backtrack(0, [], [], 0)

    dic = {tuple(tuples[i]):None for i in range(len(tuples))}

    # We now parallelize the computations of the MEBs
    with ProcessPoolExecutor() as executor:
        future_to_simplex = {executor.submit(MEB, simplex[i]): tuples[i] for i in range(len(tuples))}
        for future in as_completed(future_to_simplex):
            corresponding_tuple = tuple(future_to_simplex[future])
            filtration_value = future.result()[1]
            if filtration_value < l:
              dic[corresponding_tuple] = filtration_value
            else:
              dic.pop(corresponding_tuple)

    return dic
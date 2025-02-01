# In this file, we enumerate the number of simplexes of dimension at most k and whose filtration value is at 
# most l of the alpha complex of a set P of points in R^d.

from alpha_complexes.is_in_alpha_complex import is_in_alpha_complex
import numpy as np

def alpha_simplexes(P, l, k):
  """
  Computes every simplex of the alpha-complex of S with dimension <= k and filtration <= l.
  S : set of points of dimension d
  l : maximal filtration value
  k : maximum number of points in the simplex
  """
  n = len(P)
  lim = min(k, n) + 1
  tuples = []
  filtrations = []

  def backtrack(idx, curpoints, ind_curpoints, filtration):
    """
    Recursive backtracking function to find simplexes with filtration < l.
    """
    nonlocal n, tuples, filtrations
    if len(curpoints)> lim or filtration > l :
      return
    
    if idx == n:
      if curpoints and filtration <= l:
        tuples.append(ind_curpoints)
        filtrations.append(filtration)
      return

    backtrack(idx + 1, curpoints, ind_curpoints, filtration)

    new_curpoints = curpoints + [P[idx]]
    new_ind_curpoints = ind_curpoints + [idx]
    flag, r = is_in_alpha_complex(P, new_curpoints)
    if flag:
      backtrack(idx + 1, new_curpoints, new_ind_curpoints, max(filtration, r))
    else :
      return

  backtrack(0, [], [], 0)
  dic = dict(zip([tuple(tupl) for tupl in tuples], filtrations))
  return dic

if __name__ == '__main__':
  P = np.random.rand(10, 3)
  dic = alpha_simplexes(P, 0.5, 5)
  for tupl, fil in dic.items():
    print(f"Simplex: {tupl} --> Filtration value: {fil:.3f}")
# In this file, we enumerate the number of simplexes of dimension at most k  and whose filtration value is at most l of the alpha complex of a set P of points in R^d.

from alpha_complexes.is_in_alpha_complex import is_in_alpha_complex
from itertools import combinations
import gudhi as gd
import numpy as np

def alpha_simplexes(P, l, k):
  """
  Computes every simplex of the alpha-complex of S with dimension < k and filtration < l.
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
    #print(f"idx : {idx}, curpoints : {curpoints}, ind_curpoints : {ind_curpoints}, filtration : {filtration}")
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

def alpha_simplexes2(P, l, k):
  """
  Computes every simplex of the alpha-complex of S with dimension < k and filtration < l.
  S : set of points of dimension d
  l : maximal filtration value
  k : maximum number of points in the simplex
  """
  n = len(P)
  lim = min(k, n) + 1
  simplices = {}

  for dim in range(1, lim + 1):
      for simplex in combinations(range(n), dim):  # Génère les indices des points du simplex
          points = [P[i] for i in simplex]
          flag, r = is_in_alpha_complex(P, points)
          if flag and r <= l:
              simplices[simplex] = r  # Stocke le simplex et sa filtration

  return simplices

def alpha_simplexes3(P, l, k):
    """
    Computes every simplex of the alpha-complex of P with dimension < k and filtration < l.
    P : set of points of dimension d
    l : maximal filtration value
    k : maximum number of points in the simplex
    """
    n = len(P)
    lim = min(k, n)  # Maximum allowed simplex size
    tuples = []
    filtrations = []

    def backtrack(idx, curpoints, ind_curpoints, filtration):
        """
        Recursive backtracking function to find simplexes with filtration < l.
        """
        if len(curpoints) > lim or filtration > l:
            return
        
        # Add the current simplex if it is valid (ignoring the empty case)
        if curpoints:
            tuples.append(tuple(ind_curpoints))  # Store indices instead of points
            filtrations.append(filtration)

        for next_idx in range(idx, n):  # Ensure combinations, not permutations
            new_curpoints = curpoints + [P[next_idx]]
            new_ind_curpoints = ind_curpoints + [next_idx]
            flag, r = is_in_alpha_complex(P, new_curpoints)  # Check if valid
            if flag:
                backtrack(next_idx + 1, new_curpoints, new_ind_curpoints, max(filtration, r))

    backtrack(0, [], [], 0)
    return dict(zip(tuples, filtrations))

if __name__ == '__main__':
  #P = [[5,3,2],[4,7,6],[9,3,1],[4,7,3], [8,-4,-2], [-5,2,3], [7,1,-8]]
  P = np.random.rand(10, 3)
  dic = alpha_simplexes3(P, 0.5, 5)
  alpha_complex = gd.AlphaComplex(points=P)

  simplex_tree = alpha_complex.create_simplex_tree(max_alpha_square=0.5**2)
  simplices = simplex_tree.get_simplices()
  filtered_simplices = [
  simplex for simplex in simplices
  if len(simplex[0]) <= 6 and simplex_tree.filtration(simplex[0]) <= 0.5**2 # List of tuples (simplex (as a list), filtration value) WATCH OUT: in Gudhi, the filtration value is squared
  ]
  print(f"Our length : {len(dic)}, Gudhi length : {len(filtered_simplices)}")
  for tupl, fil in dic.items():
    if list(tupl) not in [simplex[0] for simplex in filtered_simplices]:
      print(f"Simplex {tupl} not in Gudhi \n")
      print(f"Simplex {tupl} has filtration value {fil} but Gudhi has {simplex_tree.filtration(tupl)} \n")
  for simplex in filtered_simplices:
    if tuple(simplex[0]) not in dic.keys():
      print(f"Simplex {simplex[0]} not in ours")
      print(f"Simplex {simplex[0]} has filtration value {simplex_tree.filtration(simplex[0])}")
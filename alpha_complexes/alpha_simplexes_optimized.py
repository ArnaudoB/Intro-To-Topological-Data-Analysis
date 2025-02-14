# In this file, we write an optimized version of the alpha_simplexes function using parallelization and
# range searching

from simplexes.simplexes_with_kdtree_parallelism import simplexes_kdtree_parallelism
from alpha_complexes.alpha_simplexes import alpha_simplexes

def alpha_simplexes_optimized(P, l, k):
    return simplexes_kdtree_parallelism(P, l, k, algorithm=alpha_simplexes)
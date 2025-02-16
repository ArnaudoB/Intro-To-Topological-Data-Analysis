# In this file, we enumerate naively the simplexes of dimension at most k whose filtration value 
# of the Cech complex of a set of points in R^d is inferior to a given limit l. The algorithm is less 
# naive as it uses the fact that that if a simplex is not in the complex, no simplex containing it can 
# be in the complex.

from meb.meb import MEB

def simplexes(P, l, k):
    n = len(P)
    lim = min(k, n) + 1
    tuples = []
    filtrations = []

    def backtrack(idx, curpoints, ind_curpoints, filtration): # We add a list filtrations to store the filtration values of the simplexes for optimization purposes
        """
        Recursive backtracking function to find simplexes with filtration < l.
        """
        nonlocal n, tuples, filtrations
        if len(curpoints)> lim or filtration >= l: # Simplex with more than k + 1 vertices
            return
        
        if idx == n:
            if curpoints and filtration < l:
                tuples.append(ind_curpoints)
                filtrations.append(filtration)
            return

        new_ind_curpoints = ind_curpoints + [idx]
        new_curpoints = curpoints + [P[idx]]
        new_filtration = MEB(new_curpoints)[1]
        backtrack(idx + 1, new_curpoints, new_ind_curpoints, new_filtration)

        backtrack(idx + 1, curpoints, ind_curpoints, filtration)

    backtrack(0, [], [], 0)
    dic = dict(zip([tuple(tupl) for tupl in tuples if tupl != []], filtrations))
    return dic
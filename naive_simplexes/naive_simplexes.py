# In this file, we enumerate naively the simplexes of dimension at most k of the Cech complex of a set 
# of points in R^d using a regular backtracking algorithm.


from meb.meb import MEB

def naive_simplexes(P, k):
    """
    Given a set of n points in R^d, enumerates the simplexes of dimension at most k (hence having at most
    k + 1 vertices) of the Cech complex of P and their filtration value.
    """
    n = len(P)
    lim = min(k, n) + 1
    tuples = []
    filtrations = []

    def backtrack(idx, curpoints, ind_curpoints):
        nonlocal n, tuples, filtrations
        if len(curpoints)> lim: # Simplex with more than k + 1 vertices
            return
        if idx==n:
            if curpoints:
                tuples.append(ind_curpoints)
                filtrations.append(MEB(curpoints)[1])
            return
        backtrack(idx+1, curpoints + [P[idx]], ind_curpoints + [idx])
        backtrack(idx+1, curpoints, ind_curpoints)

    backtrack(0, [], [])
    dic = dict(zip([tuple(tupl) for tupl in tuples], filtrations))
    return dic

if __name__ == '__main__':
  P = [[5,0,1],[-1,-3,4],[-1,-4,-3],[-1,4,-3]]
  dic = naive_simplexes(P, 2)
  for tupl, fil in dic.items():
    print(f"Simplex: {tupl} --> Filtration value: {fil:.3f}")
import multiprocessing
from scipy.spatial import KDTree
from simplexes.simplexes import simplexes
import numpy as np

def simplexes_kdtree_parallelism(P, l, k, algorithm=simplexes):
    """
    Given a set P of in R^d, enumerates the simplexes of dimension at most k (hence having at most k + 1 vertices) 
    and having a filtration value at most l of the Čech complex of P using parallelism to speed up the computations 
    and the use of a KDTree for range-searching.
    """
    def algorithm_embedded(P, l, k, return_dict, idx_process, indices_of_points):
        subcomplexes = algorithm(P, l, k) # dictionary {simplex (list of ints) : filtration_value}
        
        # We store the result in the shared dictionary
        return_dict[idx_process] = [(tuple(sorted([indices_of_points[id] for id in subcomplex])), filtration_value) for subcomplex, filtration_value in subcomplexes.items()]

    P = np.array(P)
    nb_points = len(P)
    kdtree = KDTree(P)

    # We initialize an array to keep track of all the seen points
    seen = [False] * nb_points

    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    jobs = []
    idx_process = 0

    for i, p in enumerate(P):
        if not seen[i]:

            # We first mark as seen every point that is at distance at most l from p
            indices_1l = kdtree.query_ball_point(p, l)
            for idx in indices_1l:
                seen[idx] = True

            # We then compute the points that are at distance at most 2*l from p to form a set of candidates points
            indices_2l = kdtree.query_ball_point(p, 2*l)
            subset_P = P[indices_2l]

            # We then launch a process to compute the simplexes of the subset of points
            p = multiprocessing.Process(target=algorithm_embedded, args=(subset_P, l, k, return_dict, idx_process, indices_2l))
            jobs.append(p)
            idx_process += 1
            p.start()
            
    # We then aggregate the results
    result_dict = {}
    for id_job in range(len(jobs)):
        jobs[id_job].join()
        for subcomplex, filtration_value in return_dict[id_job]:
            if result_dict.get(subcomplex) is None:
                result_dict[subcomplex] = filtration_value

    return result_dict
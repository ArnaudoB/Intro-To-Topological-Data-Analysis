import os
from naive_simplexes.naive_simplexes import naive_simplexes

def plot_simplexes_3d(P, simplexes):
    """
    Given a list of points and a list of simplexes (tuples of points), plots them.
    """
    
    with open('coord.txt', 'w') as f:
        for point in P:
            f.write(f"{point[0]} {point[1]} {point[2]}\n")
    
    with open('cplx.txt', 'w') as s:
        for simplex in simplexes:
            s.write(" ".join(map(str, simplex)) + "\n")
    
    os.system("./sc.py --complex cplx.txt --coordinates coord.txt plot3d")

if __name__ == '__main__':
    P = [[5,0,1], [-1,-3,4], [-1,-4,-3], [-1,4,-3]]
    tuples, _ = naive_simplexes(P, 4)
    plot_simplexes_3d(P, tuples)

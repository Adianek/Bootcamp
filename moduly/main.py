# from mathematica import geometry
# from mathematica import algebra

from mathematica.geometry import figures
from mathematica.algebra import matrices

mathematica.geometry.figures.square_area()
mathematica.algebra.matrices.add_matrices()

a = [[1]]
b = [[2]]
c = matrices.add_matrices(a, b)
print(c)

from sympy import *
from sympy.polys.orderings import monomial_key

x, y, z = symbols('x y z')

print(groebner([x**2 + y**2 + z**2 - 1, x**2 + y**2 + z**2 - 2*x, 2*x - 3*y - z], x, y, z, order='lex'))

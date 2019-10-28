from sympy import *
from sympy.polys.orderings import monomial_key

x, y, z = symbols('x y z')

print(groebner([-x**3 + y, x**2 * y - z], x, y, z, order='lex'))

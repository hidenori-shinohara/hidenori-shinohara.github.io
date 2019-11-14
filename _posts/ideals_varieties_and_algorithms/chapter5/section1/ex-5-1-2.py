from sympy import *
from sympy.polys.orderings import monomial_key

x, y, z, a = symbols('x y z a')

print(groebner([x - a * a + a, y - a * a, z - a + 3 * a * a], a, z, y, x, order='lex'))

from sympy import *
from sympy.polys.orderings import monomial_key

x, y, z = symbols('x y z')

print(groebner([x * x + y * y + z * z - 4, x * x - 2 * y * y - 5, x * z - 1], x, y, z, order='lex'))

from sympy import *
from sympy.polys.orderings import monomial_key

x, y, z = symbols('x y z')

print(groebner([x*y - 1, x*z - 1], x, y, z, order='lex'))

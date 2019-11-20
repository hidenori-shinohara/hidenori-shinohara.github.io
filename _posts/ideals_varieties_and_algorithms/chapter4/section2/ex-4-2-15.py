from sympy import *
from sympy.polys.orderings import monomial_key

x, y, z = symbols('x y z')

print(groebner([x*y, x*z, y*z], x, y, z, order='lex'))

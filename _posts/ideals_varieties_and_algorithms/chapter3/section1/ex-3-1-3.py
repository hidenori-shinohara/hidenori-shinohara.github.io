from sympy import *
from sympy.polys.orderings import monomial_key

x, y = symbols('x y')

print(groebner([x**2 + 2*y**2 - 2, x**2 + x*y + y**2 - 2], x, y, order='lex'))

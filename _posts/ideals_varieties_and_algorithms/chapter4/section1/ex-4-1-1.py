from sympy import *
from sympy.polys.orderings import monomial_key

x, y = symbols('x y')

print(groebner([x**2 + y**2 - 1, y - 1], x, y, order='lex'))

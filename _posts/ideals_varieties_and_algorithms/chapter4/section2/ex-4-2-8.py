from sympy import *
from sympy.polys.orderings import monomial_key

x, y = symbols('x y')

print(groebner([y * y + 2 * x * y - 1, x * x + 1], x, y, order='lex'))

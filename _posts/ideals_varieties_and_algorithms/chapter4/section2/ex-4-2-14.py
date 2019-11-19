from sympy import *
from sympy.polys.orderings import monomial_key

x, y, a = symbols('x y a')

print(groebner([x*y, (x - y)*x], x, y, a, order='lex'))

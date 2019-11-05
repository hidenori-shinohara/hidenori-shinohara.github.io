from sympy import *
from sympy.polys.orderings import monomial_key

x, y = symbols('x y')

print(groebner([x**2 + 2*y**2 - 3, x**2 + x*y + y**2 - 3], x, y, order='lex'))
print(groebner([x**2 + 2*y**2 - 3, x**2 + x*y + y**2 - 3], y, x, order='lex'))

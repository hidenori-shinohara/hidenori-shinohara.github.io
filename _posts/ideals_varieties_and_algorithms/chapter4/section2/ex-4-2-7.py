from sympy import *
from sympy.polys.orderings import monomial_key

x, y, z, a = symbols('x y z a')

print(groebner([x**3, y**3, x*y*(x + y), 1 - a * (x + y)], x, y, z, a, order='lex'))
print(groebner([x + z, x**2*y, x - z**2, 1 - a * (x**2 + 3*x*z)], x, y, z, a, order='lex'))

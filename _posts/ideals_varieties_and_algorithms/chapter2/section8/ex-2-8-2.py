from sympy import *
from sympy.polys.orderings import monomial_key

x, y, z = symbols('x y z')

print(groebner([x * z - y, x * y + 2 * z * z, y - z], x, y, z, order='lex'))

f1 = x*z - z
f2 = y - z
f3 = 2*z**2 + z

print(expand((x**3 * z - 2 * y**2) - (f1 * (x**2 + x + 1) + f2 * (-2*y - 2*z) + f3 * (-1))))

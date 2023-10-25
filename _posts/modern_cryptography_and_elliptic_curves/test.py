from sympy import symbols, Pow, Poly

x, a, b = symbols('x a b')
m = Poly(Poly(3 * a * a, a) / Poly(2 * b, b))
n = Poly(Poly(b, b) - Poly(Poly(3 * a * a * a, a) / Poly(2 * b, b)))
k = Poly(b * b - Pow(a, 3), a, b)

div = Poly(x - a, x, a)

y = Poly(x**3 - m**2 * x**2 - 2*m*n*x + k - n*n, x, a, b)

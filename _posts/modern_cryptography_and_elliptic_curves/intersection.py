import sympy

x, a, b, k = sympy.symbols('x a b k')

# dy/dx = 3x^2 / (2y)
#
# Therefore, the slope of the tangent line
# at (a, b) is (3a^2) / (2b).
#
# y-intercept = b - [slope] * a = (2b^2 - 3a^3) / (2b)
#
#
# Now plug
# k = b^2 - a^3
# y = [slope] x + y-intercept
# into y^2 = x^3 + k.
# Multiply each side by 4b^2

y = 3*a*a*x - 3*a*a*a + 2*b*b
xCubedPlusK = 4*b*b*(x*x*x + b*b - a*a*a)
div = x - a

# Prints -9*a**4 + 8*a*b**2 + 4*b**2*x
print(sympy.simplify((xCubedPlusK - y*y) / div / div))

# We have 0 = (9*a^4 - 8a(b^2) - 4(b^2)x)(x - a)^2
# Therefore, the last root is (9(a^4) - 8a(b^2)) / 4(b^2)
# Use b^2 = a^3 + k to get
# (a^4 - 8ak) / (4b^2)
# In other words, this is the x coordinate of the other intersection.


# Finally, plug this x coordinate into y = [slope]x + [y-intercept]
# Multiply both sides by 8(b^3) while using b**2 = a**3 + k whenever appropriate.

yTimesEightBCubed =  (3 * a**2) * (a**4 - 8 * a * k)
bSquared = a**3 + k
yInterceptTimesEightBCubed = 4 * bSquared * (2 * bSquared - 3 * a**3)

# Prints -a**6 - 20*a**3*k + 8*k**2
print(sympy.simplify(yTimesEightBCubed + yInterceptTimesEightBCubed))



import mymath

fun = str('x**2 - 5 + 0.4**(2*x)')
x1 = float(-100)
epsilon = int(4)
iterations = int(1000)
result = mymath.calculation(fun=fun, x1=x1, epsilon=epsilon, iterations=iterations)
print(result)
import sympy as sp

def call_function(fstring):
    x= sp.symbols('x')
    y= sp.symbols('y')
    expr = sp.sympify(fstring)
    return sp.lambdify((x, y), expr, "math")

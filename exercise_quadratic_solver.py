def my_sqrt(x):
    """Computes the square root of x, using the Newton-Raphson method"""
    approx = None
    guess = x / 2
    while approx != guess:
        approx = guess
        guess = (approx + x / approx) / 2
    return approx

def my_sqrt_fixed(x):
    assert 0 <= x
    if x == 0:
        return 0
    return my_sqrt(x)

def quadratic_solver(a, b, c):
    if a == 0:
        if b == 0:
            return "None"
        solution = -c / b
        return solution
    q = b * b - 4 * a * c
    if q == 0:
        solution = -b / (2 * a)
        return solution
    if q < 0:
        return "None"
    solution_1 = (-b + my_sqrt_fixed(q)) / (2 * a)
    solution_2 = (-b - my_sqrt_fixed(q)) / (2 * a)
    return (solution_1, solution_2)


from ExpectError import ExpectTimeOut

with ExpectTimeOut(1):
    my_sqrt_fixed(float('inf'))



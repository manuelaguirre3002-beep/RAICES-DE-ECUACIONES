import math
import matplotlib.pyplot as plt

def f(x):
    return x**3 - math.exp(0.8 * x) - 20.0

def df(x):
    return 3.0 * x**2 - 0.8 * math.exp(0.8 * x)

def bisection(func, a, b, tol=1e-8, max_iter=100):
    fa = func(a)
    fb = func(b)
    if fa * fb > 0:
        raise ValueError("Interval does not change sign")
    c = (a + b) / 2.0
    for i in range(max_iter):
        c = (a + b) / 2.0
        fc = func(c)
        if abs(fc) < tol or (b - a) / 2.0 < tol:
            return c, i + 1
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return c, max_iter

def newton(func, dfunc, x0, tol=1e-8, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = func(x)
        dfx = dfunc(x)
        if dfx == 0:
            return x, i + 1
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
    return x, max_iter

def secant(func, x0, x1, tol=1e-8, max_iter=100):
    x_prev = x0
    x = x1
    f_prev = func(x_prev)
    f_curr = func(x)
    for i in range(max_iter):
        if f_curr == f_prev:
            return x, i + 1
        x_new = x - f_curr * (x - x_prev) / (f_curr - f_prev)
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x_prev, x = x, x_new
        f_prev, f_curr = f_curr, func(x)
    return x, max_iter

if __name__ == "__main__":
    tol = 1e-8

    r1_b, it1_b = bisection(f, 2.0, 4.0, tol)
    r2_b, it2_b = bisection(f, 7.0, 8.0, tol)

    r1_n, it1_n = newton(f, df, 3.0, tol)
    r2_n, it2_n = newton(f, df, 8.0, tol)

    r1_s, it1_s = secant(f, 2.0, 4.0, tol)
    r2_s, it2_s = secant(f, 7.0, 8.0, tol)

    print("Ejercicio 1: x^3 - exp(0.8 x) - 20 = 0")
    print("Root near [2,4]:")
    print("  Bisection:", r1_b, "iterations:", it1_b)
    print("  Newton   :", r1_n, "iterations:", it1_n)
    print("  Secant   :", r1_s, "iterations:", it1_s)
    print("Root near [7,8]:")
    print("  Bisection:", r2_b, "iterations:", it2_b)
    print("  Newton   :", r2_n, "iterations:", it2_n)
    print("  Secant   :", r2_s, "iterations:", it2_s)

    xs = [0.0 + i * (8.0 / 1000.0) for i in range(1001)]
    ys = [f(x) for x in xs]

    plt.figure()
    plt.plot(xs, ys, label="f(x)")
    plt.axhline(0.0, linestyle="--")
    plt.scatter([r1_b, r1_n, r1_s], [0.0, 0.0, 0.0], marker="o", label="roots near 3.2")
    plt.scatter([r2_b, r2_n, r2_s], [0.0, 0.0, 0.0], marker="x", label="roots near 7.5")
    plt.title("Ejercicio 1: comparison of methods")
    plt.legend()
    plt.grid(True)
    plt.show()

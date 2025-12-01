import math
import matplotlib.pyplot as plt

def f(x):
    return math.cos(x)**2 - 0.5 * x * math.exp(0.3 * x) + 5.0

def df(x):
    return -2.0 * math.cos(x) * math.sin(x) - 0.5 * math.exp(0.3 * x) * (1.0 + 0.3 * x)

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

    r_b, it_b = bisection(f, 3.0, 4.0, tol)
    r_n, it_n = newton(f, df, 3.5, tol)
    r_s, it_s = secant(f, 3.0, 4.0, tol)

    print("Ejercicio 4: cos(x)^2 - 0.5 x exp(0.3 x) + 5 = 0")
    print("  Bisection:", r_b, "iterations:", it_b)
    print("  Newton   :", r_n, "iterations:", it_n)
    print("  Secant   :", r_s, "iterations:", it_s)

    xs = [3.0 + i * ((4.0 - 3.0) / 1000.0) for i in range(1001)]
    ys = [f(x) for x in xs]

    plt.figure()
    plt.plot(xs, ys, label="f(x)")
    plt.axhline(0.0, linestyle="--")
    plt.scatter([r_b], [0.0], marker="o", label="bisection root")
    plt.scatter([r_n], [0.0], marker="x", label="newton root")
    plt.scatter([r_s], [0.0], marker="s", label="secant root")
    plt.title("Ejercicio 4: comparison of methods")
    plt.legend()
    plt.grid(True)
    plt.show()

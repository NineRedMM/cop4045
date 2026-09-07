"""Solve and graph quadratic equations entered by the user."""

import math

import matplotlib.pyplot as plt


_NUM_POINTS = 150


def _make_domain(a, b, roots):
    """Returns an x-domain that satisfies the homework graph requirements."""
    if roots:
        xmin = min(roots)
        xmax = max(roots)

        if xmin == xmax:
            margin = max(2.0, abs(xmin) * 0.5 + 1.0)
        else:
            margin = max(2.0, (xmax - xmin) * 0.5)

        return xmin - margin, xmax + margin

    x_opt = -b / (2 * a)
    return x_opt - 5.0, x_opt + 5.0


def _plot_quadratic(a, b, c, roots):
    """Plots the quadratic function using 150 points."""
    xmin, xmax = _make_domain(a, b, roots)
    step = (xmax - xmin) / (_NUM_POINTS - 1)

    xs = [xmin + index * step for index in range(_NUM_POINTS)]
    ys = [a * x**2 + b * x + c for x in xs]

    plt.figure()
    plt.plot(xs, ys)
    plt.axhline(0)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("y = {}x^2 + {}x + {}".format(a, b, c))
    plt.grid(True)
    plt.show()


def main():
    """Repeatedly reads, solves, and plots quadratic equations."""
    while True:
        a_text = input("Enter a: ")
        if a_text == "":
            break

        a = float(a_text)
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))

        discriminant = b**2 - 4 * a * c
        roots = []

        if discriminant < 0:
            print("no real solutions")
        elif discriminant == 0:
            x1 = -b / (2 * a)
            roots = [x1]
            print("one solution: {:.5f}".format(x1))
        else:
            sqrt_discriminant = math.sqrt(discriminant)
            x1 = (-b - sqrt_discriminant) / (2 * a)
            x2 = (-b + sqrt_discriminant) / (2 * a)
            roots = [x1, x2]
            print("two solutions: x1={:.5f} x2={:.5f}".format(x1, x2))

        _plot_quadratic(a, b, c, roots)


if __name__ == "__main__":
    main()
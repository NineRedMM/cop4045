"""Display a table and plot a user-entered mathematical function."""

import math

import matplotlib.pyplot as plt


def plot_function(fun_str, domain, ns):
    """Prints sampled values and plots the function over the given domain."""
    xmin, xmax = domain
    step = (xmax - xmin) / (ns - 1)

    xs = [xmin + index * step for index in range(ns)]
    ys = []

    for x in xs:
        # The homework explicitly requires eval() for the function string.
        y = eval(fun_str)  # pylint: disable=eval-used
        ys.append(y)

    print("{:>12} {:>12}".format("x", "y"))
    print("{:>12} {:>12}".format("-" * 10, "-" * 10))

    for x, y in zip(xs, ys):
        print("{:+12.4f} {:+12.4f}".format(x, y))

    plt.figure()
    plt.plot(xs, ys, marker=".")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(fun_str)
    plt.grid(True)
    plt.show()


def main():
    """Reads function information from the terminal and plots it."""
    fun_str = input("Enter function with variable x: ")
    ns = int(input("Enter number of samples: "))
    xmin = float(input("Enter xmin: "))
    xmax = float(input("Enter xmax: "))

    plot_function(fun_str, (xmin, xmax), ns)


if __name__ == "__main__":
    main()
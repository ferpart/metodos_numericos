""" main """

from sympy import Symbol
from methods import Methods

def main():
    """ main method used for obtaing a root of a formula """

    x_value = Symbol("x")
    function = x_value**4 - x_value - 10

    mtd = Methods(function, x_value, n_iter=100)
    mtd.bisection_method(1, 2)
    mtd.regula_falsi(1, 2)
    mtd.newton_method(2)
    mtd.secant_method(1, 2)

if __name__ == "__main__":
    main()

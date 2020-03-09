""" main """

from methods import Methods

def function(x_value):
    """ function to find a root for """
    return x_value**4 - x_value -10

def function_prime(x_value):
    """ prime of function """
    return 4*x_value**3 - 1

def main():
    """ main method used for obtaing a root of a formula """
    mtd = Methods(function, n_iter=100)
    mtd.newton_method(2, function_prime)
    mtd.secant_method(1, 2)
    mtd.bisection_method(1, 2)
    mtd.regula_falsi(1, 2)

if __name__ == "__main__":
    main()

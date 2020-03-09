""" Function root finder class """

class Methods():
    """ class containing all the root finding methods """

    def __init__(self, function, exp_err=0.001, n_iter=10):
        self.exp_err = exp_err
        self.n_iter = n_iter
        self.function = function
        self.error_a = 0

    def newton_method(self, x_0, function_prime):
        """ method used to implement the newton raphson method for obtaining a function's root """

        self.error_a = 101
        i = 0
        while i < self.n_iter and self.exp_err < self.error_a:

            x_1 = x_0-self.function(x_0)/function_prime(x_0)

            if x_1 != 0:
                self.error_a = error_formula(x_0, x_1)

            x_0 = x_1
            i += 1

            print("Current iteration for newton method is %d, with root value of %.4f" %(i, x_0))
        print("Final result using the newton method is %.4f with %d iterations" %(x_0, i))

    def secant_method(self, x_0, x_1):
        """ method used to implement the secant method for obtaining a function's root """

        self.error_a = 101
        i = 0
        while i < self.n_iter and self.exp_err < self.error_a:

            if x_1 != 0:
                self.error_a = error_formula(x_0, x_1)

            if self.error_a < self.exp_err:
                break

            x_temp_upper = self.function(x_1)*(x_0-x_1)
            x_temp_lower = self.function(x_0)-self.function(x_1)

            x_0 = x_1
            x_1 = x_1-(x_temp_upper/x_temp_lower)
            i += 1

            print("Current iteration for secant method is %d, with root value of %.4f" %(i, x_1))
        print("Final result using the secant method is %.4f with %d iterations" %(x_1, i))

    def bisection_method(self, x_0, x_1):
        """ method used to implement the bisection method for obtaining a function's root """

        self.error_a = 101
        i = 0
        x_old = x_0
        while i < self.n_iter and self.exp_err < self.error_a:

            x_temp = (x_0 + x_1)/2

            if x_temp != 0:
                self.error_a = error_formula(x_temp, x_old)

            test_func = self.function(x_0)*self.function(x_temp)

            if test_func < 0:
                x_1 = x_temp
            elif test_func > 0:
                x_0 = x_temp
            else:
                self.error_a = 0

            x_old = x_temp
            i += 1

            print("Current iteration for bisection method is %d, with root value of %.4f"
                  %(i, x_old))
        print("Final result using the bisection method is %.4f with %d iterations" %(x_old, i))

    def regula_falsi(self, x_0, x_1):
        """ method used to implement the bisection method for obtaining a function's root """

        self.error_a = 101
        x_old = x_0
        i = 0
        while i < self.n_iter and self.exp_err < self.error_a:

            x_temp_upper = x_0*self.function(x_1)-x_1*self.function(x_0)
            x_temp_lower = self.function(x_1)-self.function(x_0)
            x_temp = x_temp_upper / x_temp_lower

            if x_temp != 0:
                self.error_a = error_formula(x_temp, x_old)

            test_func_1 = self.function(x_0)*self.function(x_temp)
            test_func_2 = self.function(x_1)*self.function(x_temp)

            if test_func_1 >= 0:
                x_0 = x_temp
            elif test_func_2 >= 0:
                x_1 = x_temp
            else:
                self.error_a = 0

            x_old = x_temp
            i += 1
            print("Current iteration for regula falsi is %d, with root value of %.4f"
                  %(i, x_old))
        print("Final result using regula falsi is %.4f with %d iterations" %(x_old, i))


def error_formula(x_0, x_1):
    """ method used for calculating the error in the actual iteration """

    return abs((x_1-x_0)/x_1)*100

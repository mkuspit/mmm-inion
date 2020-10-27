### import libraries
import math


### media transformation functions


def s_shape(x, a, b):
    """
    Returns an S-shaped curve Y = (X ^ a) / ((X ^ a) + (b ^ a))
    a interpretation - higher 'a' means steeper growth
    b interpretation - f(b) = 1/2
    """
    return ((x ** a) / ((x ** a) + (b ** a)))


def dim_returns(x, a):
    """
    Returns an diminishing returns curve Y = 1 - exp(-X / a)
    a interpretation - lower 'a' means steeper growth
    """
    return (1 - math.exp(-x / a))


def ad_stock(x, factor):
    """
    Returns an ad-stocked vector from vector x with defined ad-stock factor
    """
    ad_stock_vector = []
    for n in range(len(x)):
        if n == 0:
            ad_stock_vector.append(x[n])
        else:
            ad_stock_vector.append(x[n] + ad_stock_vector[n-1] * factor)
    return ad_stock_vector
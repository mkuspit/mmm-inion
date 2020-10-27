### import libraries
import math

### media transformation functions


def s_shape(x, a, b):
    """
    Returns an S-shaped curve Y = (X ^ a) / ((X ^ a) + (b ^ a))
    a interpretation - higher 'a' means steeper growth
    b interpretation - f(b) = 1/2
    For a = b = 0 returns original value
    """
    if a == 0 and b == 0:
        return x
    else:
        return ((x ** a) / ((x ** a) + (b ** a)))


def dim_returns(x, a):
    """
    Returns an diminishing returns curve Y = 1 - exp(-X / a)
    a interpretation - lower 'a' means steeper growth
    """
    return (1 - math.exp(-x / a))


def ad_stock(x, factor=0):
    """
    Returns an ad-stocked vector from vector x with defined ad-stock factor
    """
    ad_stock_vector = []
    ad_stock_value = 0
    for single_row in x:
        ad_stock_value = single_row + ad_stock_value * factor
        ad_stock_vector.append(ad_stock_value)
    return(np.array(ad_stock_vector))
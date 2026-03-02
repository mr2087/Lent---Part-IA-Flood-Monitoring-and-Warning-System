import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def polyfit(dates, levels, p):

    # Convert datetime objects to floats
    x = mdates.date2num(dates)
    # Choose a reference time to improve numerical stability
    d0 = x[0]
    x_shifted = x - d0

    # Fit a polynomial of degree p to x_shifted, levels
    polynomial_coeff = np.polyfit(x_shifted, levels, p)

    # Use coefficients to create a poly1d object
    poly = np.poly1d(polynomial_coeff)

    return poly, d0


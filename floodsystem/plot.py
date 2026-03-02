import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from floodsystem.analysis import polyfit

def plot_water_level_with_fit(station, dates, levels, p):

    # Convert datetime objects to floats
    x = mdates.date2num(dates)
    
    poly, d0 = polyfit(dates, levels, p)
    
    # Smooth the fitted curve
    smooth_x = np.linspace(x.min(), x.max(), 200)

    # Shift the smooth x-values
    x_shifted = smooth_x - d0
    # Evaluate polynomial
    smooth_y = poly(x_shifted)

    smooth_dates = mdates.num2date(smooth_x)

    # Plot raw data, add labels and title
    plt.plot(dates, levels, '.', label="Water level data")
    plt.plot(smooth_dates, smooth_y, label=f"Polynomial fit: degree {p}")

    plt.xlabel("Date")
    plt.ylabel("Water level (m)")
    plt.title(f"Water levels at {station.name}")

    plt.legend()
    plt.tight_layout()
    plt.show()
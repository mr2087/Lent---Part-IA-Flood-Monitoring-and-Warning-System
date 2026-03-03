import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from floodsystem.analysis import polyfit

### TASK 2E
def plot_water_level(station : list, dates : list, levels) -> None:
    # fdates = mdates.date2num(dates)

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(dates, levels, '.', label="Water level data")

        # default styling, may change later
    # Add axis labels, rotate date labels and add plot title
    ax.set_xlabel('date')
    ax.set_ylabel('water level (m)')
    ax.set_title(f"Station {station.name}")

    plt.xticks(rotation=45)

    # Display plot
    plt.legend()
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()

def get_water_level_fit(dates, levels, p):
    return polyfit(dates, levels, p)

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

import matplotlib.pyplot as plt

from floodsystem.station import MonitoringStation

from pprint import pprint

def plot_water_levels(station : list[MonitoringStation], dates, levels):
    pprint(dates, levels)
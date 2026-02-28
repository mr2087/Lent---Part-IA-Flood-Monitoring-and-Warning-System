from .station import MonitoringStation
from .debug import Debug
debug_util = Debug('log/a.txt')
import numpy as np

# Task2B (2)
def stations_level_over_threshold(
    stations: list[MonitoringStation], 
    tol):
    
    # Create list for the tuples
    result = []

    # Loop through each station
    for station in stations:
        level = station.relative_water_level()
        # Add tuples to list
        if level is not None and level > tol:
            result.append((station, level))

    # Sort list by relative level in descending order
    result.sort(key=lambda x: x[1], reverse=True)

    return result

# Task2C
def stations_highest_rel_level(
    stations: list[MonitoringStation],
    N):

    # Create list
    result = []
    
    # Loop through each station
    for station in stations:
        level = station.relative_water_level()
        if level is not None:
            result.append((station, level))

    # Sort list by relative level in descending order
    result.sort(key=lambda x: x[1], reverse=True)

    return result[:N]


    
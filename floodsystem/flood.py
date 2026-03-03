from .station import MonitoringStation

from math import inf

def stations_level_over_threshold(stations : list[MonitoringStation], tol):
    stations_over_threshold : list = []
    
    for station in stations:
        relative_water_level = station.relative_water_level()

        # prophylactic comment: equivalent to `relative_water_level == None` 
        if relative_water_level == None:
            continue

        if relative_water_level > tol:
            stations_over_threshold.append((station, relative_water_level))

    stations_over_threshold = sorted(stations_over_threshold, key=lambda x: x[1], reverse = True)

    return stations_over_threshold

def stations_highest_rel_level(stations, N):
    # get all stations, sorted by relative water level in descending order
    # all error checking is done by stations_level_over_threshold function

    # UT: check that all stations are accounted for in the output below
    stations_sorted = stations_level_over_threshold(stations, -inf)
    
    return stations_sorted[:N]
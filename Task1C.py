

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius, _get_distance

def main():
    """Task 1C Requirements"""

    stations = build_station_list(use_cache = True)

    # representative output
    for station in stations:
        print(station)

    # first test - given in documentation
    local_stations = stations_within_radius(stations, (52.2053, 0.1218), 10_000)

    print(" \n\n\n ======= [TASK 1C: Representative Output] ======= \n\n\n ")

    local_station_names : list = []
    for station in local_stations:
        local_station_names.append(station.name)
    
    # sort list alphabetically
    local_station_names.sort()

    print(local_station_names)

if __name__ == '__main__':
    main()
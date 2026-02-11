import sys
import pytest

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

from floodsystem.station import MonitoringStation

def main():
    """Task 1C Requirements"""

    stations = build_station_list(use_cache = True)

    # representative output
    # for station in stations:
    #     print(station)

    # first test - given in documentation
    local_stations = stations_within_radius(stations, (52.2053, 0.1218), 10_000)

    print(" \n\n\n ======= [TASK 1C.A: Output] ======= \n\n\n ")

    local_station_names : list = []
    for station in local_stations:
        local_station_names.append(station.name)
    
    # sort list alphabetically
    local_station_names.sort()

    print(local_station_names)

def test_2():
    """PYTEST - Latitude Error Logic"""
    fake_stations = [
            MonitoringStation('---', '---', 'Station A', (54.184923, -5.2848), None, 'River A', 'Town A'), # correct   
            MonitoringStation('---', '---', ['Station B', 'Alt Station B'], (19.583742, -33.1592), None, 'River B', 'Town B'),   # correct, tests return of multiple labels
            MonitoringStation('---', '---', 'Station C', (89.247194, -98.1945), None, 'River C', 'Town C')  # incorrect latitude value
        ]

    fake_local_stations = stations_within_radius(fake_stations, (52.2053, 0.1218), 10_000)

    with pytest.raises(ValueError):
        raise ValueError("asdf")
        stations_within_radius(fake_stations, (52.2053, 0.1218), 100_000)


if __name__ == '__main__':
    try:
        debug_flag = bool(sys.argv[1])
    except IndexError:
        debug_flag = False

    main(DEBUG=debug_flag)
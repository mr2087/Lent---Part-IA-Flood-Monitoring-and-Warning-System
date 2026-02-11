import pytest

from floodsystem.stationdata import build_station_list
# Import my function
from floodsystem.geo import stations_by_distance

# for unit testing
from floodsystem.geo import _get_distance

def dem_program():
    # Input Cambridge city centre coordinate, which will be p
    cambridge_centre = (52.2053, 0.1218)
    # Build the list of MonitoringStation objects that will be input to my function
    stations = build_station_list()
    # Use my function to sort by distance
    stations_with_distance = stations_by_distance(stations, cambridge_centre)
    # Get 10 closest stations
    closest_10 = stations_with_distance[:10]
    furthest_10 = stations_with_distance[-10:]
    
    print("Closest 10 stations:")
    for station, dist in closest_10:
        print((station.name, station.town, dist))
    
    print("Furthest 10 stations:")
    for station, dist in furthest_10:
        print((station.name, station.town, dist))

# PYTEST Unit Tests
def test_1B1():
    stations = build_station_list()
    cambridge_cc = (52.2053, 0.1218)
    
    # test of function
    stations_distance_sort = stations_by_distance(stations, cambridge_cc)

    # check that stations are actually sorted, m1
    for i in range(len(stations_distance_sort)-1):
        assert stations_distance_sort[i][1] <= stations_distance_sort[i+1][1]

    # check that stations are sorted, m2
    test_stations_distance = sorted(stations_distance_sort, key = lambda x : x[1])
    assert test_stations_distance == stations_distance_sort
    
if __name__ == "__main__":
    dem_program()

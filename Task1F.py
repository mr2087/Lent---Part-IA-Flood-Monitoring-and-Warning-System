from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

# for unit test
from floodsystem.station import MonitoringStation

def stations_with_inconsistent_typical_range():
    
    # Get list of stations
    stations = build_station_list()
    
    # Get list of stations with inconsistent data using my function
    inconsistent = inconsistent_typical_range_stations(stations)

    # Sort in alphabetical order
    station_names = sorted(station.name for station in inconsistent)
    
    print(station_names)

def test_1F1():
    stations = build_station_list(use_cache = True)

    # test written function
    inconsistent_stations = inconsistent_typical_range_stations(stations)

def test_1F2():
    # manual testing
    
    stations = [
        MonitoringStation('---', '---', 'Station A', (0, 0), None, '', ''),         # data totally not present, should trip
        MonitoringStation('---', '---', 'Station B', (0, 0), (1.0, None), '', ''),     # data partially not present, should trip
        MonitoringStation('---', '---', 'Station C', (0, 0), (1.2, 3.5), '', ''),    # data alright, should not trip
        MonitoringStation('---', '---', 'Station D', (0, 0), (0, 0.0), '', ''),      # could happen in practice, should not trip
        MonitoringStation('---', '---', 'Station E', (0, 0), (2.7, 2.6), '', ''),     # inconsistent data
        MonitoringStation('---', '---', 'Station F', (0, 0), (1.4, -2.3), '', '')       # should work with negative numbers, should trip
    ]

    inconsistent_stations = inconsistent_typical_range_stations(stations)

    for station in stations:
        if station.name in ['Station A', 'Station B', 'Station E', 'Station F']:
            assert station in inconsistent_stations
        else:
            assert station not in inconsistent_stations

if __name__ == "__main__":
    stations_with_inconsistent_typical_range()

    

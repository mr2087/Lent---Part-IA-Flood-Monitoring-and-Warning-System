from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def stations_with_inconsistent_typical_range():
    
    # Get list of stations
    stations = build_station_list()
    
    # Get list of stations with inconsistent data using my function
    inconsistent = inconsistent_typical_range_stations(stations)

    # Sort in alphabetical order
    station_names = sorted(station.name for station in inconsistent)
    
    print(station_names)

if __name__ == "__main__":
    stations_with_inconsistent_typical_range()

    

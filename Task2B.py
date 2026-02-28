from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
# Import my function
from floodsystem.flood import stations_level_over_threshold

def run():
    # Set defined tolerance
    tol = 4
    # Build the list of MonitoringStation objects that will be input to my function
    stations = build_station_list()
    update_water_levels(stations)
    # Use my function to print the name of the required stations and relative level
    stations_level = stations_level_over_threshold(stations, tol)
    
    for station, level in stations_level:
        print(station.name, level)

if __name__ == "__main__":
    run()
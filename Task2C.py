from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
# Import my function
from floodsystem.flood import stations_highest_rel_level

def run():
    # Set defined tolerance
    N = 10
    # Build the list of MonitoringStation objects that will be input to my function
    stations = build_station_list()
    update_water_levels(stations)
    # Use my function to print the name of the required stations and relative level
    risk_stations = stations_highest_rel_level(stations, N)
    
    for station, level in risk_stations:
        print(station.name, level)

if __name__ == "__main__":
    run()
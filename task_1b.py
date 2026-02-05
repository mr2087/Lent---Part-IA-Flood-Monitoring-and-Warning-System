from floodsystem.stationdata import build_station_list
# Import my function
from floodsystem.geo import stations_by_distance

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
    
if __name__ == "__main__":
    dem_program()

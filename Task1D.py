from floodsystem.stationdata import build_station_list
# Import my function
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def dem_program_d1():
    # Build the list of MonitoringStation objects that will be input to my function
    stations = build_station_list()
    # Use my function to print rivers
    rivers = rivers_with_station(stations)
    # Sort the rivers alphabetically
    rivers = sorted(rivers)
    # Get first 10 rivers 
    first_10 = rivers[:10]

    print("Number of rivers with at least one monitoring station", len(rivers))
    print("First 10 rivers:", first_10)
    
def test_1D1():
    stations = build_station_list()

    # check function
    rivers = rivers_with_station(stations)

def dem_program_d2():
    # Build the list of MonitoringStation objects that will be input to my function
    stations = build_station_list() 
    # Use my function to print stations
    river_dictionary = stations_by_river(stations)
    
    # Include stations whose river name contains 'Aire', 'Cam' or 'Thames' 
    for river in ["Aire", "Cam", "Thames"]:

        # Get station names from any dictonary key that contains the substring
        station_names = sorted(
            station.name 
            # Loop through every river name 
            for key, stations_list in river_dictionary.items()
            # Select any river that matches the conditions specified above
            if river in key
            # Loop through all stations for each of these rivers
            for station in stations_list
        )
        print(f"Stations on {river}")
        print(station_names)   
       
def task_1D2():
    stations = build_station_list()

    # test function
    rivers : dict = stations_by_river()

    # make sure all stations have been accounted for
    tot_stations : int = 0
    for bound_stations in rivers.values():
        tot_stations += len(bound_stations)
    assert tot_stations == len(stations)

if __name__ == "__main__":
    dem_program_d1()
    dem_program_d2()
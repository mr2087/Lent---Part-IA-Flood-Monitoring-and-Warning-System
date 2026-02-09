from .station import MonitoringStation
from .debug import Debug
debug_util = Debug('log/a.txt')

from math import sin, cos, asin, sqrt, pi

from .utils import sorted_by_key

# better to use this type for all "coordinate"-like objects for the sake of clarity
#   must always be given in the form (latitude, longitude)
Coordinate = tuple

def _hav(theta : float) -> float:
    """Implementation of the haversine `hav x = sin^2(x/2)`."""

    return (sin(theta / 2)) ** 2


def _get_distance(
    coord_1 : Coordinate,
    coord_2 : Coordinate,
) -> float:
    """Given two `Coordinates` in latitude-longitude form, returns the distance 
    between the two coordinates on Earth in metres using the haversine.

    **Note:** This implementation uses duck typing for the two input parameters; 
    as such, there is no internal verification. Hence, improperly formatted 
    coordinate values may return incorrect or nonsensical values!  

    @param coord_1: The first `Coordinate`.
    @param coord_2: The second `Coordinate`.
    """
    # convert into radians
    lat1 = coord_1[0] * pi/180
    lng1 = coord_1[1] * pi/180
    lat2 = coord_2[0] * pi/180
    lng2 = coord_2[1] * pi/180

    # calculate haversine of coordinates
    delta_latitude  : float = lat2 - lat1
    delta_longitude : float = lng2 - lng1

    haversine : float = _hav(delta_latitude) + cos(lat1)*cos(lat2)*_hav(delta_longitude)
    assert 0 <= haversine <= 1
    
    # get angle from haversine
    central_angle : float = 2 * asin(sqrt(haversine))

    # get distance with formula `d = R*angle`, R in metres
    # we approximate earth as perfect sphere
    earth_radius : float = 6371 * 1000
    distance : float = earth_radius * central_angle

    return distance

# for task 1B
def stations_by_distance(
    stations: list[MonitoringStation], 
    p : Coordinate):
    # Build a list of (station_object, distance_from_p) tuples 
    result =[]
    
    # Loop through every MonitoringStation object in the input list
    for station in stations:
        # Each station has a .coord attribute that can be used in this function
        # Compute the distance between the station and coordinate p
        distance = get_distance(p, station.coord)
        # Store pair (station_object, distance_from_p) by adding it to the end of the list
        result.append((station, distance))
    
    # Sort the list by the distance_from_p, which is the second element of each tuple
    result = sorted_by_key(result, 1)

    return result

# for task 1C
def get_stations_within_radius(
    stations : list[MonitoringStation],
    centre : Coordinate,
    r : float
) -> list[MonitoringStation]:
    """Implementation of the main logic for Task 1C. 
    
    Given the list of stations, a centre coordinate and radius, returns a list
    of stations which are closer to the centre than the radius. All coordinates
    are expected in `(latitude, longitude)` format. 
    Distances between two points are calculated with the haversine formula.

    @param stations: The `list` of `MonitoringStations` on which the stations within the given radius are to be returned.
    @param centre:   The `tuple` in `Coordinate` format which represents the latitude and longitude of the central point.
    @param r:        The `float` which gives the maximum filtering radius.
    """
    LATITUDE_MAX : float = +90
    LATITUDE_MIN : float = -90

    # check that all stations are indeed MonitoringStations
    if not all([isinstance(station, MonitoringStation) for station in stations]):
        raise TypeError("[STAT::WITHIN::RADIUS] Parameter `station` improperly formatted: not all station elements are MonitoringStation")
    # check that centre coordinates are within bounds
    if not (LATITUDE_MIN <= centre[1] <= LATITUDE_MAX):
        debug_util.warn("geo::stations_within_radius", "Latitude parameter of centre not within expected interval [-90, +90].")
    if not all([LATITUDE_MIN <= station.coord[1] <= LATITUDE_MAX for station in stations]):
        debug_util.warn("geo::stations_within_radius", "Latitude parameter of station not within expected interval [-90, +90].")
    if not (isinstance(r, float) or isinstance(r, int)):
        raise TypeError

    stations_within_radius : list[MonitoringStation] = []

    # get distances to all stations from centre
    for station in stations:
        station_centre = station.coord

        # uses haversine formula
        distance = _get_distance(centre, station_centre)

        # check if distance is less than upper bound r
        if distance <= r:
            stations_within_radius.append(station)

    return stations_within_radius

# for task 1D
def rivers_with_station(
    stations: list[MonitoringStation]):
    # Build a set to fill with the names of rivers with a monitoring station
    # A set was chosen because a set contains no duplicate elements
    result = set()
    
    # Loop through every MonitoringStation object in the input list
    for station in stations:
        # Add every river with a monitoring station to the result set
        result.add(station.river)
    return result

def stations_by_river(
    stations: list[MonitoringStation]):
    # Create an empty dictionary
    dictionary = {}
    # Loop through each station to get rivers
    for station in stations:
        river = station.river

        # If river not seen before (not in dictionary), create a new list
        if river not in dictionary:
            dictionary[river] = []
        # Add station to the list for this river
            dictionary[river].append(station)
    
    return dictionary

# for task 1E
def rivers_by_station_number(
    stations : list[MonitoringStation], 
    N : int
) -> list[tuple[str, int]]:
    """Implementation of the main logic for Task 1E.
    
    Given a list of stations, and a limit `N`, returns the `N` rivers with the 
    most associated stations. Return type is a `list` of a `tuple`, where the 
    inner `tuple` should be seen in the form `(river name, number of stations)`.
    
    If there exists more than one river with the same number of stations at 
    the `N`th position, then this implementation returns all sucn rivers. 
    Note therefore that the length of the returned `list` must not be `N`, 
    it may be smaller (if number of rivers is less than `N`) or larger 
    (if the edge case described above occurs).

    @param stations: The `list` of `MonitoringStations` from which the river station data is to be determined.
    @param N: An `int` which describes the upper bound of rivers to be returned.
    """
    # count rivers in stations
    river_station_count : dict = {}

    for station in stations:
        station_river = station.river

        # river already present in `river_station_count` check
        if station_river not in river_station_count.keys():
            # river is not registered yet
            river_station_count[station_river] = 1      
        else:
            # river is already registered
            river_station_count[station_river] += 1     

    # sort river station count by number of stations descending
    river_station_count = {station : count 
                           for station, count 
                           in sorted(
                               river_station_count.items(), 
                               key=lambda x : x[1],
                               reverse=True)
                          }
    river_count_data : list = list(river_station_count.items())
    print(river_count_data)

    i = 0
    # edge cases on the number of rivers
    if N > len(river_count_data):
        return river_count_data
    elif N == 0:
        return []

    # here we will not run out of river data
    else:
        rivers_station_number : list = []

        # terminates if upper bound is reached and 
        # there are no ties in station count
        while i < N or \
              river_count_data[i][1] == river_count_data[i-1][1]:
            
            rivers_station_number.append(river_count_data[i])
            i += 1
    
        return rivers_station_number
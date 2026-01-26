from station import MonitoringStation

from math import sin, cos, asin, sqrt

# better to use this type for all "coordinate"-like objects for the sake of clarity
#   should always be given in the form (latitude, longitude)
Coordinate = tuple

def hav(theta : float) -> float:
    """Implements the explicit haversine formula `hav x = sin^2(x/2)`."""

    return (sin(theta / 2)) ** 2


def get_distance(
    coord_1 : Coordinate,
    coord_2 : Coordinate,
) -> float:
    """Given two coordinates in latitude-longitude form, returns the distance 
    between the two coordinates on Earth in metres using the haversine.
    
    """
    # add defense later ... 

    # calculate haversine of coordinates
    delta_latitude  : float = coord_2[0] - coord_1[0]
    delta_longitude : float = coord_2[1] - coord_1[0]

    haversine : float = hav(delta_latitude) + cos(coord_2[0])*cos(coord_1[0])*hav(delta_longitude)
    assert 0 <= haversine <= 1
    
    # get angle from haversine
    central_angle : float = 2 * asin(sqrt(haversine))

    # get distance with formula `d = R*angle`
    earth_radius : float = 6371 * 1000          # given in metres
    distance : float = earth_radius * central_angle

    return distance

# for task 1C
def get_stations_within_radius(
    stations : list[MonitoringStation],
    centre : Coordinate,
    r : float
) -> list[MonitoringStation]:
    # duck type centre and r

    stations_within_radius : list[MonitoringStation] = []

    # get distances to all stations from centre
    for station in stations:
        station_centre = station.coord

        distance = get_distance(centre, station_centre)

        # check if distance is less than upper bound r
        if distance <= r:
            stations_within_radius.append(station)

    return stations_within_radius


# for task 1E
def rivers_by_station_number(
    stations : list[MonitoringStation], 
    N : int
) -> list[tuple[str, int]]:
    # count rivers in stations
    river_station_count : dict = {}

    for station in stations:
        station_river = station.river

        if station_river not in river_station_count.keys():
            river_station_count[station_river] = 1
        else:
            river_station_count[station_river] += 1

    # sort river station count by number of stations descending
    river_station_count = {station : count 
                           for station, count 
                           in sorted(
                               river_station_count.items(), 
                               key=lambda x : x[1],
                               reverse=True)
                          }
    river_count_data : list = river_station_count.items()
    
    # return the appropriate number of rivers
    i = 0
    if N > len(river_count_data):
        return river_count_data
    elif N == 0:
        return []
    else:
        rivers_station_number = []

        # here we will not run out of river data
        while i < (N-1) or \
              river_count_data[i][1] == river_count_data[i+1][1]:
            
            rivers_station_number.append(river_count_data[i])
    
        return rivers_station_number